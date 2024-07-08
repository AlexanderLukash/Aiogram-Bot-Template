FROM python:3.12.3-slim-bullseye

WORKDIR /app/bot

COPY pyproject.toml /app/bot

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/bot