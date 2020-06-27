FROM python:3.7.7-stretch

WORKDIR /home/rest-python

COPY pyproject.toml poetry.lock ./

RUN mkdir outputs -p \
    && pip install poetry \
    && poetry export --dev -f requirements.txt > outputs/requirements.txt \
    && pip install -r outputs/requirements.txt
