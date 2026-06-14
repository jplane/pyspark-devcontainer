# Local PySpark dev environment

This repo provides a self-contained, local PySpark development environment that runs on your laptop with Docker, VS Code, and Dev Containers.

It uses [Visual Studio Code](https://code.visualstudio.com/) and the [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) feature to run Spark and JupyterLab in Docker while keeping the workspace mounted in your editor.

## Requirements

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Install [Visual Studio Code](https://code.visualstudio.com/download)
- Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension

## Setup

1. Clone this repository to your laptop.
2. Open the repo folder in VS Code.
3. Run the VS Code command palette command `Dev Containers: Reopen in Container`.
4. Wait for the container to build. The `postCreateCommand` installs the project and development tools from `pyproject.toml`.
5. Open [test.ipynb](./test.ipynb) in VS Code.
6. Use the JupyterLab interface at `http://localhost:8888`.
7. If the notebook asks for a kernel, select the `vscode_pyspark` kernel.
8. Run the cells in order to explore the local Spark session.

## Development tooling

The project now includes modern Python tooling for local checks and CI:

- `ruff` for linting
- `black` for formatting
- `pytest` for tests
- `pre-commit` for consistent hooks

You can run the checks locally with:

```bash
python -m pip install -e '.[dev]'
ruff check .
black --check .
pytest
```

## Notes

- The devcontainer now uses a pinned base image (`jupyter/pyspark-notebook:spark-3.5.0`) for reproducible builds.
- The Spark UI is exposed on port `4040` for debugging and monitoring.

