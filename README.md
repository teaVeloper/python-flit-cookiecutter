# Python flit cookiecutter

this is my (Bertold) project template for python using flit as build and packaging tool.

The idea is to build a template with sensible defaults, that can nicely be used as is.
Things can easily be added or removed as needed!

Some options will be asked from cookiecutter and maybe something is available as template to look at, but not active


to bootstrap the python venv after initializing the cookiecutter, just run make install
maybe there will be an optional cookiecutter hook for that!

## Development tools
It uses these development tools

### src - layout

I follow the 'src - layout' as detailed [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/)
TLDR: your tests are not testing your setup but the one an install would look like

### pyproject.toml

a pyproject.toml file as the means to configure everything possible. No setup.py or setup.cfg

### Build & Packaging

[flit](https://flit.pypa.io/en/stable/) as build and packaging tool
because its easy and painless to use

[pip-tools](https://pip-tools.readthedocs.io/en/latest/) to pin version numbers and get dependency inheritance

[bumpver](https://gitlab.com/mbarkhau/pycalver) for bumping versions, it supports both semver and calver
set up:
- semver
- commit, tag

### Test Framework

[pytest](https://docs.pytest.org/en/7.4.x/) as the testing framework

### Code Quality

[mypy](https://docs.pytest.org/en/7.4.x/) for static type analysis


[isort](https://docs.pytest.org/en/7.4.x/) to automatically align the imports


[black](https://black.readthedocs.io/en/stable/) as the autoformatter
 - line length 120

[ruff](https://docs.astral.sh/ruff/) as linter
with some settings:
 - line length 120
 - ignore unused imports (F401) in __init__.py

### Helpers

[invoke](https://www.pyinvoke.org/) for some helpful tasks as:
- test - run test suite
- clean - delete all temporary files
- code-quality - check, only boolean
- lint - run linter and get analytics
- format - autoformat with black and isort
- build
- publish
- bump [major, minor, patch] version, autocreate commit and tag
- compile requirements files

[Makefile](https://www.gnu.org/software/make/) for convenience whats not possible in invoke?
- bootstrap project
- create venv
- delete distclean (delete all data and venv)
- run invoke tasks with venv

for simplicity the venv will be created in folder .venv - any other things need adaption! 
(e.g. using virtualenvwrapper)

[gitlab-ci](https://docs.gitlab.com/ee/ci/) some gitlab ci pipelines for
 - running code-quality
 - running tests
 - build & publish

[pre-commit](https://pre-commit.com/) for some git hooks, comes pre-configured with some helpful ones
but needs to be installed locally


### Optional?

to maybe be done in some later versions!

[sphinx](https://www.sphinx-doc.org/en/master/) for documentation - maybe not

[asdf](https://asdf-vm.com/) a `.tools-versions` file with specific versions for that project
maybe alternatively also 
[direnv](https://direnv.net/) for folder specific settings


## TODO:

pypirc or publish options, also 2 registries, azure and gitlab
