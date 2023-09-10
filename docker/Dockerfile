FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.5.1

ENV PYTHONPATH=/app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --without=dev --no-interaction --no-ansi

COPY docker/gunicorn_conf.py /gunicorn_conf.py

COPY ./app /app/app

CMD ["gunicorn", "-k uvicorn.workers.UvicornWorker", "-c", "/gunicorn_conf.py", "app.main:create_app()"]
