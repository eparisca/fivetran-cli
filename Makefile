PYTHON_BASE = python3.13
VENV = .venv
UV := uv
PYTHON := $(UV) run python
PIP = $(UV) pip
PYTEST := $(UV) run pytest
COVERAGE := $(UV) run coverage
RUFF := $(UV) run ruff

.DEFAULT_GOAL := help

fivetran:
	echo "#!/usr/bin/env bash" > fivetran
	echo 'uv run ./src/cli.py "$${@}"' >> fivetran
	chmod +x fivetran

.PHONY: lock
lock:  ## Lock all requirements.
	$(UV) lock

.PHONY: clean
clean:  ## Clean-up the project
	rm -rf $(VENV)
	rm -rf .ruff_cache
	rm -f fivetran
	rm -rf dist
	rm -rf fivetran_cli.egg-info

$(VENV):  ## Create virtualenv if it doesn't exist.
	if [ ! -d "$(VENV)" ]; then \
		$(UV) venv --python $(PYTHON_BASE); \
	else \
		echo "Virtualenv already exists."; \
	fi; \

.PHONY: install-dev
install-dev: $(VENV)  ## Install the test dependencies
	$(UV) add --editable . --dev


.PHONY: install
install: $(VENV) fivetran  ## Install the project dependencies
	$(UV) sync

# .PHONE: install-dev
# install-dev: install  ## Install the development dependencies
# # 	$(UV) add --editable . --dev
# 	$(PIP) install -e .

.PHONY: format
format: ruff-format isort  ## Run formatters

.PHONY: ruff-format
ruff-format:  ## Run the ruff formatter
	$(RUFF) format ./src

.PHONY: isort
isort:  ## Run isort formatter
	$(PYTHON) -m isort --profile=black --atomic ./src

.PHONY: ruff-lint
ruff-lint:  ## Run the ruff linter
	$(RUFF) check ./src

.PHONY: lint
lint: ruff-lint  ## Run the linters

.PHONY: test
test:  ## Run the tests
	$(PYTEST) ./tests

.PHONY: help
help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'