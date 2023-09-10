# FastAPI starter

This repository is to be used as a starter for FastAPI based Python applications.

## Features

- [Python3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/latest/)

## Prerequisites

- [Python3.11+](https://www.python.org/)
- [Poetry](https://python-poetry.org/) for project management
- [Docker](https://docs.docker.com/) for image builds


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

-  `poetry install`- creates virtualenv and installs project dependencies
-  `poetry lock`- updates `poetry.lock`
-  `poetry update`- updates packages locally and updates `poetry.lock`

## Project tasks list (uses taskipy to execute, example: `poetry run task isort`)
-  `isort`- sort imports
-  `black`- run black on project files
-  `tests`- execute tests
-  `format-and-lint`- shortcut of all three of the above
-  `run-app-local`- launches app locally
