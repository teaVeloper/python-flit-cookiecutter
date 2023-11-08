VIRTUALENV_VERSION := $(shell virtualenv --version 2>/dev/null)

ifdef VIRTUALENV_VERSION
	VENV_COMMAND := virtualenv
else
	VENV_COMMAND := python -m venv
endif

VENV_PATH := .venv
INVOKE := ${VENV_PATH}/bin/invoke
PIP := ${VENV_PATH}/bin/python -m pip
PYTHON := ${VENV_PATH}/bin/python
FLIT := ${VENV_PATH}/bin/flit

# all:

.PHONY: install clean distclean publish test format lint check delete_venv build

install:
# create venv and install program in there
# use virtualenv if available, fallback to venv if not
	${VENV_COMMAND} ${VENV_PATH}
	${PIP} install flit
	${FLIT} install -s


clean:
# not delete venv
	${INVOKE} clean

delete_venv:
	rm -rf .venv

distclean: clean delete_venv
# delete venv

# copy from tasks, but run inside venv
#
build:
	${INVOKE} build

publish:
	${INVOKE} publish

test:
	${INVOKE} test

format:
	${INVOKE} format

lint:
	${INVOKE} lint

check:
	# code quality
	${INVOKE} code-quality

test-debug:
	pytest --pdb --pdbcls=IPython.terminal.debugger:TerminalPdb
