[:var_set('', """
# Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:HDLR('heading', 'heading')]\
# AoikProjectStarter-Python
Python project starter that can tidy-lint-test code and build documentation in
one command.

Uses [Waf](https://github.com/waf-project/waf) as build system, supports
incremental build.

Integrates these tools:
- Build tools
    - pyenv
    - waf
    - pip
    - virtualenv
    - tox
- Tidying tools
    - autoflake
    - autopep8
    - isort
- Linting tools
    - pyflakes
    - flake8
    - pycodestyle
    - pydocstyle
    - pylint
- Testing tools
    - unittest
    - nose
    - nose2
    - pytest
    - doctest
    - coverage
    - lettuce
    - robotframework
- Documentation tools
    - sphinx

Tested working with:
- Linux, Windows
- Python 2.7, 3.5

![Image](https://raw.githubusercontent.com/AoiKuiyuyou/AoikProjectStarter-Python/0.1.0/screenshot/screenshot.gif)

## Table of Contents
[:hd_to_key('toc')]\
[:toc(beg='next', indent=-1)]

## Setup
Clone this repository to local:
```
git clone https://github.com/AoiKuiyuyou/AoikProjectStarter-Python aoikprojectstarter
```

## Usage
[:tod()]

### Set up pyenv
Windows users can skip this step.

For Linux users, it is recommended not to change system Python's packages.
Instead, use pyenv to build Python versions independent of the system Python.
Follow [these steps](/tools/pyenv/README.md) to set up pyenv.

### Change working directory
Change working directory to `waf`:
```
cd aoikprojectstarter/tools/waf
```

Notice commands below are run in this directory.

### Generate initial configuration
`Waf` requires generating an initial configuration before other `Waf` commands
can be run. This is analogous to running `configure` for a project using `make`
as build system.

Run:
```
python waf.py configure
```

### Show available commands
Run:
```
python waf.py --help
```

### Set up pip
Run:
```
python waf.py pip_setup
```

`pip` and `virtualenv` are the only two packages that will be set up in the
current Python program's packages environment. All other packages will be set
up in virtual environment.

If the current Python is system Python, root permission is needed to make
changes to the system Python's packages environment. Using pyenv can avoid this
issue.

### Set up virtualenv
Run:
```
python waf.py virtualenv_setup
```

`pip` and `virtualenv` are the only two packages that will be set up in the
current Python program's packages environment. All other packages will be set
up in virtual environment.

If the current Python is system Python, root permission is needed to make
changes to the system Python's packages environment. Using pyenv can avoid this
issue.

### Set up development virtual environment
Run:
```
python waf.py dev_venv
```

### Set up production virtual environment
Run:
```
python waf.py prod_venv
```

### Set up custom virtual environment
Run:
```
python waf.py venv --venv temp_venv
```

Given virtual environment path will be postfixed with current Python full
version, e.g. `temp_venv.py3.5.1.final.0.64bit`.

If this is not desired, use option `--venv-add-version=0` to disable:
```
python waf.py venv --venv temp_venv --venv-add-version=0
```

### Run all tools to tidy code
Run:
```
python waf.py tidy
```

### Run autoflake to tidy code
Run:
```
python waf.py autoflake
```

### Run autopep8 to tidy code
Run:
```
python waf.py autopep8
```

### Run isort to tidy code
Run:
```
python waf.py isort
```

### Run all tools to lint code
Run:
```
python waf.py lint
```

### Run isort to lint code
Run:
```
python waf.py isort_check
```

### Run pyflakes to lint code
Run:
```
python waf.py pyflakes
```

### Run flake8 to lint code
Run:
```
python waf.py flake8
```

### Run pycodestyle to lint code
Run:
```
python waf.py pycodestyle
```

### Run pydocstyle to lint code
Run:
```
python waf.py pydocstyle
```

### Run pylint to lint code
Run:
```
python waf.py pylint
```

### Run all tools to test code
Run:
```
python waf.py test
```

### Run unittest to test code
Run:
```
python waf.py unittest
```

### Run nose to test code
Run:
```
python waf.py nose
```

### Run nose2 to test code
Run:
```
python waf.py nose2
```

### Run pytest to test code
Run:
```
python waf.py pytest
```

Run doc tests only:
```
python waf.py doctest
```

### Run lettuce to test code 
Run:
```
python waf.py lettuce
```

### Run robotframework to test code 
Run:
```
python waf.py robotframework
```

### Run tox to test code 
Run:
```
python waf.py tox
```

### Run all tools to build documentation
Run:
```
python waf.py doc
```

### Run sphinx to build documentation
Run:
```
python waf.py sphinx
```

### List Python files
Run:
```
python waf.py list_py
```

### Delete all files untracked in git
Run:
```
python waf.py clean
```

### Force task to run
[:tod()]

`Waf` supports incremental build. It uses dirty checking of input and output
targets (usually files) to decide whether a task (created by `Waf` command)
should be run.

Some tasks' output is hard to be declared as targets, for example using `pip`
to set up packages. The output files may be outside the project, or may be
massive or indefinite.

For such tasks, this project's `Waf` commands create touch files as output
targets for dirty checking. These touch files are put in the project's
`build_waf/.touch/` directory.

It is possible that the touch files are not changed but the real state of the
task is changed, for example using the project's `Waf` command to set up the
`virtualenv` package, and then removing the package manually.

In such situations, the task should be forced to run. There are several options
to force a task to run, which will be introduced below. It is worth noting that
these options are not native features provided by `Waf`, so care should be
taken for newly added `Waf` commands to honor these options.


#### Use option `--check-import`:
Run:
```
python waf.py virtualenv_setup --check-import
```

This option tells the `Waf` command to check whether a module of the package
that is being set up can be imported. If the module can not be imported, the
corresponding touch files will be updated to force the dirty checking to fail,
thus force the task to run to set up the package.

#### Use option `--always`:
Run:
```
python waf.py virtualenv_setup --always
```

This option tells the `Waf` command to always run the task. The `Waf` command
uses the same technique of updating the corresponding touch files to force the
task to run.

This option has larger impact than option `--check-import` does because it
forces dependency tasks to run as well.

#### Delete touch files
Deleting the corresponding touch files in the `build_waf/.touch/` directory can
force a task to run, for the same reason explained above.
