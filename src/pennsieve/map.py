"""
Pennsieve Map feature — client-side wrapper.

Mirrors the `pennsieve map` / `map pull` / `map push` / `map diff` CLI
commands that live in the Go agent. The gRPC calls return as soon as the
agent has started the work; long-running operations (pull, push) execute
in goroutines on the agent side. The `wait_for_*` helpers here let callers
block until completion when needed.
"""

from __future__ import annotations

import json
import os
import threading
import time
from pathlib import Path
from typing import Iterable, Optional

from .protos import agent_pb2


class Map:
    """Operations on a Pennsieve Mapped Dataset.

    A mapped dataset is a local folder that mirrors a Pennsieve dataset's
    tree as empty placeholder files, with a hidden `.pennsieve/` directory
    holding the workspace manifest and pull state. Users pull selected
    subfolders to get real bytes, and push to upload new files back.

    Methods:
    --------
    map(dataset_id, target_folder):
        Create a new mapped dataset at target_folder.
    pull(path):
        Download real content for files under `path` in a mapped dataset.
    push(path):
        Upload any new local files under `path` back to the mapped dataset.
    diff(path):
        Return added / changed / renamed / moved / deleted file status.
    wait_for_pull(target_folder, idle_timeout=...):
        Block until pulled files appear in state.json. Fails only if no new
        files appear within `idle_timeout` seconds — total duration unbounded.
    wait_for_push(expected_files, subscriber_id, idle_timeout=...):
        Block until upload_status COMPLETE events match expected_files. Fails
        only if no upload-status event arrives within `idle_timeout` seconds.
    """

    def __init__(self, stub):
        self._stub = stub

    # ---------- RPCs ----------

    def map(self, dataset_id: str, target_folder: str):
        """Create a new mapped dataset on disk.

        Returns a SimpleStatusResponse. The agent downloads the workspace
        manifest and creates placeholder files for every entry.
        """
        request = agent_pb2.MapRequest(
            dataset_id=dataset_id,
            target_folder=str(target_folder),
        )
        return self._stub.Map(request=request)

    def pull(self, path: str):
        """Pull real file bytes for files under `path`.

        `path` can be any file or folder inside a mapped dataset; the agent
        walks up to find the dataset root. Returns a SimpleStatusResponse
        once the pull has been kicked off — work continues in the background.
        Use `wait_for_pull` to block until it finishes.
        """
        request = agent_pb2.PullRequest(path=str(path))
        return self._stub.Pull(request=request)

    def push(self, path: str):
        """Push new local files under `path` back to the mapped dataset.

        Only ADDED files are uploaded (CHANGED / RENAMED / MOVED / DELETED
        are ignored by the agent today). Returns immediately; use
        `wait_for_push` with the expected file count to block.
        """
        request = agent_pb2.PushRequest(path=str(path))
        return self._stub.Push(request=request)

    def diff(self, path: str):
        """Return local vs. remote diff for the mapped dataset at `path`."""
        request = agent_pb2.MapDiffRequest(path=str(path))
        return self._stub.GetMapDiff(request=request)

    # ---------- wait helpers ----------

    def wait_for_pull(
        self,
        target_folder: str,
        expected_relative_paths: Optional[Iterable[str]] = None,
        idle_timeout: float = 1800.0,
        poll_interval: float = 0.5,
    ) -> None:
        """Block until expected files are pulled.

        Polls `<target_folder>/.pennsieve/state.json`. A file counts as
        pulled when it has an entry in the state file with `isLocal=true`.

        Pull only records files that were actually requested, so when
        `expected_relative_paths` is None we wait for any non-zero set of
        local files to appear — which is only useful when the caller knows
        pull has been issued against an empty prior state. Prefer passing
        the set of paths you asked to pull.

        Paths are matched against the `path` field of state.json records,
        which the agent writes with forward slashes relative to the
        dataset root.

        `idle_timeout` is the max seconds allowed between progress events
        (a new file appearing in state.json). The deadline resets each time
        the local-files set grows, so total duration is unbounded — fits
        TB/PB-scale pulls where a single file can take hours. Raises
        TimeoutError only if no new file appears within `idle_timeout`.
        """
        state_path = Path(target_folder) / ".pennsieve" / "state.json"
        expected: Optional[set[str]] = None
        if expected_relative_paths is not None:
            expected = {p.replace("\\", "/").lstrip("/") for p in expected_relative_paths}

        last_progress = time.monotonic()
        last_count = 0
        while True:
            local_paths = _read_local_state_paths(state_path)

            if expected is None:
                if local_paths:
                    return
            else:
                if expected.issubset(local_paths):
                    return

            if len(local_paths) > last_count:
                last_count = len(local_paths)
                last_progress = time.monotonic()

            if time.monotonic() - last_progress >= idle_timeout:
                missing = expected - local_paths if expected is not None else set()
                raise TimeoutError(
                    f"wait_for_pull: no new files in {idle_timeout}s "
                    f"(have {last_count}); "
                    f"missing {len(missing)} file(s): {sorted(missing)[:5]}"
                )
            time.sleep(poll_interval)

    def wait_for_push(
        self,
        expected_files: int,
        subscriber_id: int,
        idle_timeout: float = 300.0,
    ) -> int:
        """Block until `expected_files` upload-status COMPLETE events arrive.

        Opens a Subscribe stream against the agent and counts
        SubscribeResponse messages whose `upload_status.status` is COMPLETE
        (enum value 2). Returns the number of COMPLETE events observed
        (should equal `expected_files` on success).

        `subscriber_id` must be unique per subscriber within the agent's
        lifetime. Picking os.getpid() + a counter works for most cases.

        `idle_timeout` is the max seconds allowed between upload-status
        events (INIT / IN_PROGRESS / COMPLETE all count as progress). Each
        event resets the idle window, so total duration is unbounded — a
        multi-hour single-file upload is fine as long as the agent keeps
        emitting progress. Raises TimeoutError only when the stream goes
        silent for `idle_timeout` seconds.
        """
        completed = 0
        progress = threading.Event()
        done = threading.Event()
        error: list[BaseException] = []

        def consume():
            nonlocal completed
            try:
                request = agent_pb2.SubscribeRequest(id=subscriber_id)
                for response in self._stub.Subscribe(request=request):
                    # type==1 is UPLOAD_STATUS in the SubscribeResponse enum
                    if response.type == 1:
                        progress.set()
                        if response.upload_status.status == 2:
                            completed += 1
                            if completed >= expected_files:
                                done.set()
                                return
            except BaseException as exc:  # includes grpc.RpcError on cancel
                error.append(exc)
                done.set()

        t = threading.Thread(target=consume, daemon=True)
        t.start()

        finished = False
        while not finished:
            progress.clear()
            if done.wait(timeout=idle_timeout):
                finished = True
                break
            if not progress.is_set():
                # No upload-status event arrived during the whole window.
                break

        # Stop the subscriber so the stream closes promptly.
        try:
            self._stub.Unsubscribe(
                request=agent_pb2.SubscribeRequest(id=subscriber_id),
            )
        except Exception:
            pass

        if not finished:
            raise TimeoutError(
                f"wait_for_push: no upload-status event in {idle_timeout}s; "
                f"observed {completed}/{expected_files} COMPLETE event(s)"
            )
        if error and completed < expected_files:
            # Surface the stream error only if we didn't get enough events
            # first; otherwise the error is just the stream shutdown and
            # is expected.
            raise error[0]
        return completed


def _read_local_state_paths(state_path: Path) -> set[str]:
    """Return the set of relative paths in state.json with isLocal=True.

    Returns an empty set if the file doesn't exist or isn't yet valid JSON
    (the agent writes the file after pulling every batch; a partial write
    is rare but possible, so we treat parse errors as "not ready").
    """
    if not state_path.exists():
        return set()
    try:
        with state_path.open("r") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return set()

    out: set[str] = set()
    for record in data.get("files") or []:
        if record.get("isLocal") and record.get("path"):
            out.add(record["path"])
    return out
