import json
import threading
import time
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from pennsieve.map import Map, _read_local_state_paths
from pennsieve.protos import agent_pb2


def test_map_rpc_wraps_request_with_dataset_id_and_target():
    stub = MagicMock()
    m = Map(stub)

    m.map("N:dataset:abc", "/tmp/mapped")

    stub.Map.assert_called_once()
    req = stub.Map.call_args.kwargs["request"]
    assert isinstance(req, agent_pb2.MapRequest)
    assert req.dataset_id == "N:dataset:abc"
    assert req.target_folder == "/tmp/mapped"


def test_pull_push_diff_forward_to_stub():
    stub = MagicMock()
    m = Map(stub)

    m.pull("/tmp/mapped/folder")
    assert isinstance(stub.Pull.call_args.kwargs["request"], agent_pb2.PullRequest)
    assert stub.Pull.call_args.kwargs["request"].path == "/tmp/mapped/folder"

    m.push("/tmp/mapped")
    assert isinstance(stub.Push.call_args.kwargs["request"], agent_pb2.PushRequest)
    assert stub.Push.call_args.kwargs["request"].path == "/tmp/mapped"

    m.diff("/tmp/mapped")
    assert isinstance(stub.GetMapDiff.call_args.kwargs["request"], agent_pb2.MapDiffRequest)
    assert stub.GetMapDiff.call_args.kwargs["request"].path == "/tmp/mapped"


def _write_state(target: Path, records):
    pennsieve_dir = target / ".pennsieve"
    pennsieve_dir.mkdir(parents=True, exist_ok=True)
    (pennsieve_dir / "state.json").write_text(
        json.dumps(
            {
                "lastFetch": "2026-04-20T00:00:00Z",
                "lastPull": "2026-04-20T00:00:00Z",
                "files": records,
            }
        )
    )


def test_wait_for_pull_returns_when_expected_paths_local(tmp_path):
    m = Map(MagicMock())

    _write_state(
        tmp_path,
        [
            {"path": "folder/a.lay", "isLocal": True, "pullTime": "2026-04-20T00:00:00Z"},
            {"path": "folder/b.lay", "isLocal": True, "pullTime": "2026-04-20T00:00:00Z"},
        ],
    )

    m.wait_for_pull(
        target_folder=str(tmp_path),
        expected_relative_paths=["folder/a.lay", "folder/b.lay"],
        timeout=1.0,
        poll_interval=0.01,
    )  # must not raise


def test_wait_for_pull_times_out_when_paths_missing(tmp_path):
    m = Map(MagicMock())
    _write_state(tmp_path, [{"path": "folder/a.lay", "isLocal": True}])

    with pytest.raises(TimeoutError) as exc:
        m.wait_for_pull(
            target_folder=str(tmp_path),
            expected_relative_paths=["folder/a.lay", "folder/missing.lay"],
            timeout=0.2,
            poll_interval=0.05,
        )
    assert "folder/missing.lay" in str(exc.value)


def test_wait_for_pull_ignores_non_local_records(tmp_path):
    m = Map(MagicMock())
    _write_state(
        tmp_path,
        [
            {"path": "folder/a.lay", "isLocal": False},
            {"path": "folder/a.lay", "isLocal": True},
        ],
    )
    # Latest-wins isn't defined; presence of any isLocal=True record is enough.
    m.wait_for_pull(
        target_folder=str(tmp_path),
        expected_relative_paths=["folder/a.lay"],
        timeout=0.5,
        poll_interval=0.01,
    )


def test_wait_for_pull_polls_until_state_appears(tmp_path):
    m = Map(MagicMock())

    def write_later():
        time.sleep(0.05)
        _write_state(
            tmp_path,
            [{"path": "folder/a.lay", "isLocal": True}],
        )

    t = threading.Thread(target=write_later)
    t.start()
    try:
        m.wait_for_pull(
            target_folder=str(tmp_path),
            expected_relative_paths=["folder/a.lay"],
            timeout=1.0,
            poll_interval=0.01,
        )
    finally:
        t.join()


def test_read_local_state_paths_returns_empty_when_missing(tmp_path):
    assert _read_local_state_paths(tmp_path / "nope.json") == set()


def test_read_local_state_paths_tolerates_invalid_json(tmp_path):
    p = tmp_path / "state.json"
    p.write_text("{not valid")
    assert _read_local_state_paths(p) == set()


class _FakeSubscribeResponse:
    """Minimal duck-type for SubscribeResponse used by wait_for_push."""

    class _UploadStatus:
        def __init__(self, status):
            self.status = status

    def __init__(self, type_, upload_status_code=None):
        self.type = type_
        self.upload_status = self._UploadStatus(upload_status_code or 0)


def test_wait_for_push_counts_complete_events():
    events = [
        _FakeSubscribeResponse(type_=0),                  # general info -- ignored
        _FakeSubscribeResponse(type_=1, upload_status_code=1),  # IN_PROGRESS
        _FakeSubscribeResponse(type_=1, upload_status_code=2),  # COMPLETE #1
        _FakeSubscribeResponse(type_=1, upload_status_code=2),  # COMPLETE #2
    ]

    stub = MagicMock()

    def subscribe(request):
        for e in events:
            yield e
        # Then block so the thread doesn't exit immediately after yielding
        # (simulating a live stream).
        while True:
            time.sleep(0.05)

    stub.Subscribe.side_effect = lambda request: subscribe(request)

    m = Map(stub)
    count = m.wait_for_push(expected_files=2, subscriber_id=9001, timeout=2.0)
    assert count == 2
    stub.Unsubscribe.assert_called_once()


def test_wait_for_push_times_out_when_not_enough_events():
    stub = MagicMock()

    def subscribe(request):
        yield _FakeSubscribeResponse(type_=1, upload_status_code=2)  # one COMPLETE
        while True:
            time.sleep(0.05)

    stub.Subscribe.side_effect = lambda request: subscribe(request)

    m = Map(stub)
    with pytest.raises(TimeoutError):
        m.wait_for_push(expected_files=2, subscriber_id=9002, timeout=0.3)
