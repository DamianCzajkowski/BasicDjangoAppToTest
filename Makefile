COMPOSE_FILE=docker-compose.yml

## Common workflow commands
up:
	docker-compose -f $(COMPOSE_FILE) up --always-recreate-deps

build:
	docker-compose -f $(COMPOSE_FILE) build

down:
	docker-compose -f $(COMPOSE_FILE) down


bash:
	docker-compose -f $(COMPOSE_FILE) run --rm web bash

## Code overhaul
mypy:
	docker-compose -f $(COMPOSE_FILE) run --rm web mypy --config-file .mypy.ini .

flake:
	docker-compose -f $(COMPOSE_FILE) run --rm web flake8

isort:
	docker-compose -f $(COMPOSE_FILE) run --rm web isort .

black:
	docker-compose -f $(COMPOSE_FILE) run --rm web black . --target-version py38 -l 110

supercode: isort black flake mypy
