install:
	@poetry install

check:
	@poetry check

lint:
	@poetry run flake8 brain_games

run:
	@poetry run brain-games

.PHONY: install check lint run
