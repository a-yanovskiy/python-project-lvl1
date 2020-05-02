install:
	@poetry install

check:
	@poetry check

lint:
	@poetry run flake8 brain_games

.PHONY: install check lint
