FROM docker-registry.ebrains.eu/hdc-services-image/base-image:python-3.10.14-v1 as audit-trail-image

ENV TZ=America/Toronto \
    PYTHONDONTWRITEBYTECODE=true \
    PYTHONIOENCODING=UTF-8 \
    POETRY_VERSION=1.3.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev --no-root --no-interaction
COPY . .

RUN chown -R app:app /app
USER app

RUN chmod +x gunicorn_starter.sh

CMD ["./gunicorn_starter.sh"]
