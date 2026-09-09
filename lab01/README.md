# Lab 01: Project Status

## What it does

Reads `data/tasks.csv` and prints a project status report with the completed task
count, task names, statuses, and owners. The supplied data has 2 completed tasks
out of 5. Source code is in `src/project_status/`, tests are in `tests/`, and input
data is in `data/`.

## How to set it up

Install `uv` and use Python 3.11 or newer. From the repository root:

```sh
cd lab01
uv sync
```

This creates `.venv/`, installs the project and Ruff, and uses the versions in
`uv.lock`. Keep `pyproject.toml` and `uv.lock` in version control; the environment
and tool caches are ignored by the repository's `.gitignore`.

## How to run it

Run from the `lab01/` directory so the relative data path resolves correctly:

```sh
uv run python -m project_status
```

## How to check it

From `lab01/`:

```sh
uv run ruff format --check .
uv run ruff check .
uv run python -m unittest discover -s tests
uv run python -m project_status | diff - expected_output.txt
```

Ruff should report that all checks passed, the test should end with `OK`, and
`diff` should print nothing, confirming the output matches exactly.

To apply formatting and safe lint fixes when editing:

```sh
uv run ruff format .
uv run ruff check --fix .
```
