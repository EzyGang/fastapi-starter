FROM python:3.12-alpine AS compile-image

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    UV_PROJECT_ENVIRONMENT="/venv" \
    UV_COMPILE_BYTECODE=1

ENV PYTHONPATH=/app

RUN pip install uv
RUN apk add gcc python3-dev libc-dev

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

# Runtime
FROM python:3.12-alpine AS runtime-image

ENV UV_PROJECT_ENVIRONMENT="/venv"
ENV UV_COMPILE_BYTECODE=1
ENV PATH="$UV_PROJECT_ENVIRONMENT/bin:$PATH"
ENV PATH="/venv/bin:$PATH"

RUN pip install uv

ENV PYTHONPATH=/app
WORKDIR /app

ARG RELEASE_VERSION=0.0.0
ENV RELEASE=$RELEASE_VERSION

# Copy source and venv
COPY ./app /app/app
COPY ./docker/gunicorn_conf.py /gunicorn_conf.py
COPY --from=compile-image /venv /venv

CMD ["uv", "run", "gunicorn", "-k uvicorn_worker.UvicornWorker", "-c", "/gunicorn_conf.py", "app.main:app"]

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot

USER nonroot