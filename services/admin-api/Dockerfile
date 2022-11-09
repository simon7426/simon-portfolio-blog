ARG POETRY_VERSION=1.2.1

FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apk add --no-cache \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    curl --proto '=https' --tlsv1.2 -sSf "https://sh.rustup.rs" | sh -s -- -y --profile=minimal && \
    source $HOME/.cargo/env && \
    curl -sSL "https://install.python-poetry.org" | python - && \
    apk del \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev

ENV PATH "/root/.local/bin:$PATH"

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY . .

CMD ["poetry","run","uvicorn", "project:app", "--host", "0.0.0.0", "--port", "8000"]