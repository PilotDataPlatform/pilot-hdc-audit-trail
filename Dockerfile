FROM python:3.7-buster

ENV TZ=America/Toronto \
    PYTHONDONTWRITEBYTECODE=true \
    PYTHONIOENCODING=UTF-8 \
    POETRY_VERSION=1.3.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /usr/src/app

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get update && \
    apt-get install -y vim-tiny less && \
    ln -s /usr/bin/vim.tiny /usr/bin/vim && \
    rm -rf /var/lib/apt/lists/*

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev --no-root --no-interaction
COPY . .
RUN chmod +x gunicorn_starter.sh

CMD ["./gunicorn_starter.sh"]
