SHELL := /bin/bash
PY := poetry run python
PYTEST := ${PY} -m pytest
PYTEST_OPTS :=
MYPY := poetry run mypy
MYPY_OPTS := --strict
SRC_DIR := ./src
TEST_DIR := ./test

.PHONY: test/lint
test/lint:
	${MYPY} ${MYPY_OPTS} ${SRC_DIR}

.PHONY: test
test: test/lint
	${PYTEST} ${PYTEST_OPTS} ${TEST_DIR}
