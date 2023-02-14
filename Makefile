
PYTHON_VERSION := 3.11
PYTHON_BIN := python$(PYTHON_VERSION)

VENV_DEV := .venv-dev

$(VENV_DEV):
	$(PYTHON_BIN) -m venv $(VENV_DEV); \
		. $(VENV_DEV)/bin/activate; \
		pip install --upgrade pip; \
		pip install -e .[dev];

.git/hooks/pre-commit: $(VENV_DEV)
	. $(VENV_DEV)/bin/activate; \
		pre-commit install

.PHONY: setup-dev
setup-dev: $(VENV_DEV) .git/hooks/pre-commit

.PHONY: test
test: setup-dev
	. $(VENV_DEV)/bin/activate; \
	tox

.PHONY: clean
clean:
	rm -rf \
		$(VENV_DEV) \
		build/ \
		$(shell find -iname '*.egg-info' -type d) \
		$(shell find __pycache__ -type d) \
		$(shell find -iname .pytest_cache -type d) \
		.mypy_cache \
		.tox
