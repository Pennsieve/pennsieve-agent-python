Pennsieve Python client (pennsieve2)
================
[![PyPI Latest Release](https://img.shields.io/pypi/v/pennsieve2.svg)](https://pypi.org/project/pennsieve2/)
[![pypi](https://img.shields.io/pypi/pyversions/pennsieve2.svg)](https://pypi.org/project/pennsieve2/)
[![Package Status](https://img.shields.io/pypi/status/pennsieve2.svg)](https://pypi.org/project/pennsieve2/)
[![License](https://img.shields.io/pypi/l/pennsieve2.svg)](https://github.com/Pennsieve/pennsieve-agent-python/blob/main/LICENSE)
[![Coverage](https://codecov.io/github/pennsieve/pennsieve-agent-python/coverage.svg?branch=main)](https://codecov.io/gh/pennsieve/pennsieve-agent-python)

Python client and command line tool for Pennsieve (pennsieve2).


Prerequisites
-------------
In order to use this Python library to upload files to Pennsieve, please follow the instruction on installing and setting up Pennsieve agent, which could be found in the documentation.


Installation
------------

To install, run:

```bash
    pip install -U pennsieve
```

To install specific previous dev version, run:
```bash
    pip install -U pennsieve==0.1.0.dev2 --extra-index-url https://test.pypi.org/simple
```

Contributions
--------------

To update gRPC python files, execute from the src folder:

```bash
    rm src/pennsieve/protos/agent_pb2*
    cd src
    python3.9 -m grpc_tools.protoc --python_out=. -I. --grpc_python_out=. pennsieve/protos/agent.proto
```
Notice, this command does not produce a valid agent_pb2.py file when executed for Python3.10 or formatted by black - it does not use reflection and is reported as error for Flake8.


To create a package and upload it to PyPI, first update the package version in the pennsieve2/__init__.py, then execute:

```bash
    python -m build
    # For testing:
    twine upload -r testpypi dist/*
    # For production:
    twine upload dist/*
```

Mapped Datasets
---------------

The `client.map` wrapper exposes the agent's mapped-dataset RPCs (`map`,
`pull`, `push`, `diff`) as a small Python API. The four RPCs return as soon
as the agent has accepted the work — `pull` and `push` then run in the
background inside the agent — so `client.map` also ships two blocking
helpers: `wait_for_pull` and `wait_for_push`.

```python
client.map.map(dataset_id="N:dataset:...", target_folder="/data/foo")
client.map.pull("/data/foo/subfolder")
client.map.wait_for_pull("/data/foo", expected_relative_paths=[...])

client.map.push("/data/foo")
client.map.wait_for_push(expected_files=N, subscriber_id=os.getpid())
```

### Timeouts

Both wait helpers use an **idle timeout** rather than a total-duration
timeout — the deadline resets each time progress is observed, so a
multi-hour single-file transfer is fine as long as the agent keeps making
progress. You only hit a `TimeoutError` when the agent goes silent.

**`wait_for_pull`** — default `idle_timeout=1800` (30 min)
- *Progress signal:* a new file entry appears in `.pennsieve/state.json`, which the agent writes on each file's completion.
- *Why 30 min:* the window has to cover the worst-case single-file download end-to-end, since there is no per-chunk progress for pulls.

**`wait_for_push`** — default `idle_timeout=300` (5 min)
- *Progress signal:* any `UPLOAD_STATUS` event (`INIT` / `IN_PROGRESS` / `COMPLETE`). The agent emits `IN_PROGRESS` on every S3 chunk read, so events stream continuously during healthy uploads.
- *Why 5 min:* events are frequent during healthy uploads, so 5 minutes of silence indicates a real stall (network hang, agent wedge) rather than slow progress.

Override either default by passing `idle_timeout=<seconds>` when you know
your transfer characteristics — e.g. pulls over a very slow link with large
individual files, or tighter CI smoke-tests where you want to fail faster.

```python
client.map.wait_for_pull(target_folder, idle_timeout=3600)  # 1 hour
client.map.wait_for_push(expected_files=N, subscriber_id=..., idle_timeout=60)  # 1 minute
```

Documentation
-------------

Client and command line documentation can be found on [Pennsieve’s documentation website](https://docs.pennsieve.io/docs/uploading-files-programmatically).

Development
-------------

This project uses [Poetry](https://python-poetry.org/) to manage dependencies in `pyproject.toml`. To set up a development environment run
```bash
  poetry install
```
from the root directory to install the projects dependencies. Some IDEs (IntelliJ Idea for example) can create a Poetry Python
environment as well.

Installing from TestPypi
------------------------
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pennsieve
