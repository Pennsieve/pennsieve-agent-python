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
