PYFILES ?= $(shell find . -name "*.py" -not -path "./.venv/*" -not -path "./**/migrations/*")
POETRY_RUN ?= poetry run

# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: init
init: ## initialize
	pip install poetry
	poetry install

.PHONY: format
format: ## format codes
	$(POETRY_RUN) black $(PYFILES)
	$(POETRY_RUN) isort $(PYFILES)

.PHONY: lint
lint: ## lint codes
	$(POETRY_RUN) pylint $(PYFILES)

.PHONY: test
test: ## test codes
	$(POETRY_RUN) pytest -v ./

# Django ---

USERNAME ?= admin
EMAIL ?= admin@example.com
HOST ?= 0.0.0.0
PORT ?= 8080
OUTPUTS_DIR ?= ./outputs
WORKERS ?= 4

.PHONY: makemigrations
makemigrations: ## make migrations
	$(POETRY_RUN) python manage.py makemigrations

.PHONY: migrate
migrate: ## migrate
	$(POETRY_RUN) python manage.py migrate

.PHONY: createsuperuser
createsuperuser: ## create superuser
	$(POETRY_RUN) python manage.py createsuperuser \
		--username $(USERNAME) \
		--email $(EMAIL)

.PHONY: runserver
runserver: ## runserver
	$(POETRY_RUN) python manage.py runserver $(HOST):$(PORT)

.PHONY: collectstatic
collectstatic: ## collectstatic
	$(POETRY_RUN) python manage.py collectstatic --noinput

.PHONY: gunicorn
gunicorn: ## gunicorn
	$(POETRY_RUN) gunicorn --workers $(WORKERS) --bind 0.0.0.0:$(PORT) config.wsgi:application

.PHONY: clean
clean: ## clean outputs
	rm -rf $(OUTPUTS_DIR)/*

.PHONY: deploy
deploy: ## deploy
	make makemigrations
	make migrate
	make collectstatic
	make gunicorn

# Docker ---
SERVICE ?= python
CMD ?= bash

.PHONY: docker-run
docker-run:
	docker-compose run --rm $(SERVICE) $(CMD)

.PHONY: docker-exec
docker-exec:
	docker-compose exec $(SERVICE) $(CMD)
	
