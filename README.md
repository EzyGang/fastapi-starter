# FastAPI starter

This repository is to be used as a starter for FastAPI based Python applications.

## Features

- [Python3.12+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)

## Prerequisites

- [Python3.12+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) for project management
- [Docker](https://docs.docker.com/) for image builds (use `--target runtime-image`)


## Project Structure

```
  .
  ├── app                     # Contains code base.
  │   ├── apps                # Contains python subpackages for each registered app
  │       ├── `app_name`
  │       │   ├── api         # Contains API endpoints declaration
  │       │   ├── dtos        # Contains DTO declarations
  │       │   └── use_cases   # Contains this app's use cases
  │       └── routes.py       # Registers all routers from all applications
  │   ├── core                # Configs and settings, logging, etc
  │   └── lib                 # Contains reusable base/abstract classes, helpers, etc
  ├── docker                  # Contains docker related files
  ├── tests                   # Tests
  └── ...
```

## Useful commands

-  `uv sync`- creates virtualenv and installs project dependencies
-  `uv lock`- updates `uv.lock`
-  `uv sync --upgrade`- updates packages locally and updates `uv.lock`

## Project tasks list (uses taskipy to execute, example: `uv run task mypy-lint`)
-  `ruff` - runs ruff on a project files
-  `tests` - runs tests
-  `mypy-lint` - run mypy lint
-  `ruff-lint` - runs ruff check (to use in CI/CD)
-  `format-and-lint`- shortcut to run ruff and mypy
