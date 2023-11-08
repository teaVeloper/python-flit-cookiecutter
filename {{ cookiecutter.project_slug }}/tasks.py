from invoke.tasks import task


# helpers or sub-tasks
def _delete_files(c, files, recursive=False):
    """
    Helper for deleting files, e.g. running:
        rm -[r]f ..
    on an iterable of file/folder names
    """
    if recursive:
        flag = "-rf"
    else:
        flag = "-f"
    for file_ in files:
        cmd = f"rm {flag} {file_}"
        c.run(cmd)


def _delete_files_by_pattern(c, files_pattern, recursive=False):
    """
    Helper for deleting files, e.g. running:
        rm -[r]f ..
    on an iterable of file/folder names
    """
    if recursive:
        flag = "-rf"
    else:
        flag = "-f"
    for pattern in files_pattern:
        cmd = f"find . -name '{pattern}' -exec rm {flag}" + " {} +"
        c.run(cmd)


@task
def clean_pyc(c):
    """
    delete all python cache related files and folders
    """
    _delete_files_by_pattern(c, ["*.pyc", "*.pyo", "*~"])
    _delete_files_by_pattern(c, ["__pycache__"], recursive=True)


@task
def clean_test(c):
    """
    delete all test related files and folders
    """
    _delete_files(c, [".tox/", "htmlcov", ".pytest_cache",
                  ".mypy_cache"], recursive=True)
    _delete_files(c, [".coverage"])


@task
def clean_build(c):
    """
    delete all build related files and folders
    """
    _delete_files(c, ["._deployment/", "build/",
                  "dist/", ".eggs/"], recursive=True)
    _delete_files_by_pattern(c, ["*.egg-info"], recursive=True)
    _delete_files_by_pattern(c, ["*.egg"])


@task
def check_format(c):
    c.run("black --check src tests", pty=True)
    c.run("isort --check src tests", pty=True)


@task
def typecheck(c):
    """
    run mypy type checking optional with --check-untyped-defs (default on)
    """
    c.run("mypy src", pty=True)


@task
def compile_requirements(c):
    """
    create requirements files with pip-tools
    """
    command = "pip-compile pyproject.toml"
    common_options = "--resolver=backtracking --no-emit-index-url"
    c.run(f"{command} -o requirements.txt {common_options}")
    c.run(f"{command} --extra dev -o requirements-dev.txt {common_options}")

# "public" interface


@task(clean_pyc, clean_test, clean_build)
def clean(_):
    """
    delete all reproducible data (pycache, test, build, runs all other clean tasks)
    """


@task
def test(c):
    """
    run test suite with pytest
    """
    c.run("pytest tests", pty=True)


@task
def format(c, linting=False):
    '''
    run black and isort
    '''
    c.run("isort src tests", pty=True)
    c.run("black src tests", pty=True)
    if linting:
        lint(c, fix=True)


@task
def lint(c, fix=False):
    """
    run ruff linting
    """
    command = "ruff check src tests"
    if fix:
        command += " --fix"
    c.run(command, pty=True)


@task(check_format, lint, typecheck)
def code_quality(_):
    """
    run lint and typecheck
    check with black and isort
    """


@task
def build(c):
    """
    run build with flit
    """
    c.run("flit build", pty=True)


@task
def publish(c, pypirc=None):
    """
    run publish with flit
    """
    command = "flit publish"
    if pypirc:
        command += f" --pypirc {pypirc}"
    c.run(command, pty=True)


@task
def bump(c, patch=True, minor=False, major=False, tag=True, dry=False):
    """
    bump version and commit, optional add git tag
    """
    bumper = "bumpver update"
    if patch:
        bumper += " --patch"
    elif minor:
        bumper += " --minor"
    elif major:
        bumper += " --major"

    if tag:
        bumper += " --tag-commit"
    else:
        bumper += " --no-tag-commit"

    if dry:
        bumper += "--dry"
    c.run(bumper, pty=True)
