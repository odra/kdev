SHELL := /bin/bash
PY := @poetry run python
PYTEST := ${PY} -m pytest
PYTEST_OPTS :=
TEST_DIR := test/
MYPY := ${PY} -m mypy
MYPY_OPTS := --strict
SRC_DIR := src/

.PHONY: test/mypy
test/mypy:
	${MYPY} ${MYPY_OPTS} ${SRC_DIR}

.PHONY: test/pytest
test/pytest:
	${PYTEST} ${PYTEST_OPTS} ${TEST_DIR}

.PHONY: test
test: test/mypy test/pytest
