
PYTHON_VERSION := 3.11
PYTHON_BIN := python$(PYTHON_VERSION)

VENV_CI := .venv-ci
VENV_DEV := .venv-dev

$(VENV_DEV):
	$(PYTHON_BIN) -m venv $(VENV_DEV); \
		. $(VENV_DEV)/bin/activate; \
		pip install --upgrade pip; \
		pip install -e .[test] -r requirements-dev.txt;

$(VENV_CI):
	$(PYTHON_BIN) -m venv $(VENV_CI); \
		. $(VENV_CI)/bin/activate; \
		pip install --upgrade pip
		pip install -r requirements-ci.txt;

.git/hooks/pre-commit: $(VENV_DEV)
	. $(VENV_DEV)/bin/activate; \
		pre-commit install

.PHONY: setup-dev
setup-dev: $(VENV_DEV) .git/hooks/pre-commit

.PHONY: test
test: $(VENV_CI)
	. $(VENV_CI)/bin/activate; \
	tox

.PHONY: clean
clean:
	rm -rf \
		$(VENV_CI) \
		$(VENV_DEV) \
		build/ \
		$(shell find . -iname '*.egg-info' -type d) \
		$(shell find . -iname __pycache__ -type d) \
		$(shell find . -iname .pytest_cache -type d) \
		.mypy_cache \
		.tox
