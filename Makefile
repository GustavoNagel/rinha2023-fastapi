codestyle:
	poetry run isort --settings-path pyproject.toml ./ ; \
	poetry run black --config pyproject.toml ./

mypy:
	poetry run mypy --config-file pyproject.toml ./

test:
	poetry run pytest ; \
	poetry run coverage-badge -o assets/images/coverage.svg -f

check: codestyle mypy test

local-setup:
	poetry install --with dev

.PHONY: check local-setup test mypy codestyle
