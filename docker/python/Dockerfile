FROM python:3.7.7-stretch

WORKDIR /home/rest-python

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry install --no-dev
