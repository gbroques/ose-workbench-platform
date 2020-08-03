# OSE Workbench Platform
[![PyPI version](https://badge.fury.io/py/ose-workbench-platform.svg)](https://badge.fury.io/py/ose-workbench-platform)
[![Conda version](https://anaconda.org/gbroques/ose-workbench-platform/badges/version.svg)](https://anaconda.org/gbroques/ose-workbench-platform)
[![Build Status](https://travis-ci.org/gbroques/ose-workbench-platform.svg?branch=master)](https://travis-ci.org/gbroques/ose-workbench-platform)
[![Documentation Status](https://readthedocs.org/projects/ose-workbench-platform/badge/?version=latest)](https://ose-workbench-platform.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/gbroques/ose-workbench-platform/badge.svg?branch=master)](https://coveralls.io/github/gbroques/ose-workbench-platform?branch=master)

* [Introduction](#introduction)
* [Pre-Requisites](#pre-requisites)
* [Installation](#installation)
* [Virtual Development Environment](#virtual-development-environment)
* [Unit Tests](#unit-tests)
* [Documentation](#documentation)
* [Commands](#commands)
  * [test](#test)
  * [lint](#lint)
  * [docs](#docs)
  * [build](#build)
  * [make](#make)
  * [browse](#browse)
  * [editor-config](#editor-config)
* [Contributing](#contributing)
* [License](#license)

## Introduction
A platform for developing workbenches for Open Source Ecology (OSE).

OSE defines a "workbench" as a set of tools in CAD software to design and make a particular machine.

Each workbench OSE develops for one of it's machines has certain common development-time or "dev-time" needs and dependencies.

For example, running unit tests, making documentation, and generating code to streamline workbench development.

Rather than duplicate the approaches to each of these needs, `ose-workbench-platform` abstracts those needs into a common platform so they aren't the concern of individual OSE workbench maintainers.

Each workbench maintainer doesn't need to know or care about the particular versions and libraries we use to solve those needs, nor the particular configuration.

Having a common platform for OSE workbench development also makes it easier for developers to readily switch between workbenches by providing a common tool-set.

`ose-workbench-platform` provides a command-line interface (CLI), via the `osewb` command, containing commands for common dev-time tasks such as running all tests, making documentation, initializing new workbenches, and even generating code for common tasks.

## Pre-Requisites
1. Install [Git](https://git-scm.com/)
2. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Installation
Install the `ose-workbench-platform` package from the `gbroques` channel in a dedicated conda environment named `osewb` (short for **O**pen **S**ource **E**cology **W**ork**B**ench) and don't ask for confirmation:

    conda create --name osewb --channel gbroques --yes ose-workbench-platform

Activate your new `osewb` environment:

    conda activate osewb

Test your installation:

    osewb --help

You can deactivate this environment later by running:

    conda deactivate

## Virtual Development Environment
We use [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) to create a reproducible [virtualized OSE workbench development environment](https://en.wikipedia.org/wiki/OS-level_virtualization) with requisite dependencies for development-time tasks like running FreeCAD, executing unit tests, and generating documentation from source-code comments.

In order to perform various development-time tasks for a workbench, you must first:

1. Create a conda environment from the `environment.yml` file located in the root of the workbench repository
2. Activate the environment with `conda activate <environment name>`

Note, each workbench will have it's own separate environment.

Workbench environments will be named after the base package in the workbench repository (e.g. `ose3dprinter`, `osetractor`, `osepowercube`, etc.).

Some common commands relating to managing environments with `conda` are documented in the below table.

|Description|Command|
|-----------|-------|
|**Creating** the environment|`conda env create --file environment.yml`|
|**Activating** the environment|`conda activate <environment name>`|
|**Deactivating** the environment|`conda deactivate`|

Refer to the [Conda CLI reference documentation](https://docs.conda.io/projects/conda/en/latest/commands.html) for additional information.

## Unit Tests
For running unit tests we use [pytest](https://docs.pytest.org/en/latest/).

For test coverage, we use [coverage.py](https://coverage.readthedocs.io/en/latest/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/).

## Documentation
For building documentation, we use [Sphinx](https://www.sphinx-doc.org/en/master/).

For hosting documentation, we use a free service for **open-source** projects called [Read the Docs](https://readthedocs.org/).

For a modern and mobile-friendly look, we use [Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/).

## Commands
The `osewb` command contains various sub-commands for performing common dev-time tasks of a OSE workbench.

```
$ osewb -h ↵
usage: osewb <command> [<args>]

A collection commands for OSE workbench development.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

Commands:
  {test,lint,docs,make,browse,br}
    test                Run tests in workbench
    lint                Lint code
    docs                Make documentation
    make                Commands for making new code
    browse (br)         Commands for opening documents in a web browser
```

Each sub-command may have flags and arguments, and additional information can be discovered via `osewb <command> -h` or `--help`.

Is `osewb` too many characters to type? We recommend [aliasing](https://en.wikipedia.org/wiki/Alias_(command)) the ``osewb`` command as ``ose`` to reduce typing and increase speed even further.

For further convenience, any command over four characters shall include a short-alias under four characters or less. For example, `br` is the short-alias for the five-character `browse` command.

### test
OSE Workbench Platform includes a `test` command for interacting with the test-suite of a workbench.

```
$ osewb test -h ↵
usage: osewb test

optional arguments:
  -h, --help      show this help message and exit
  -c, --coverage  Run tests with coverage, and generate report
```

To run the entire unit-test suite for a workbench, run:

    osewb test

For running tests with coverage and generating a coverage report, pass the `-c` or `--coverage` flag to the `test` command:

    osewb test --coverage

### lint
OSE Workbench Platform includes a `lint` command for linting the code of a workbench.

    osewb lint

The `lint` command will:

* Run `flake8` with configuration located in [.flake8](./osewb/.flake8).
* Run `mypy` for static type checking with configuration located in [.mypy.ini](./osewb/.mypy.ini).

For automatically fixing *some* linter issues, pass the `-f` or `--fix` flag to the `lint` command:

    osewb lint --fix

This will run [isort](https://github.com/timothycrosley/isort) and [autopep8](https://github.com/hhatto/autopep8) recursively on the root of the workbench repository.

For additional information, see:
* [flake8](https://flake8.pycqa.org/en/latest/)
* [mypy](http://www.mypy-lang.org/)

### docs
OSE Workbench Platform includes a `docs` command for building the documentation of a workbench.

```
$ osewb docs -h ↵
usage: osewb docs [command]

optional arguments:
  -h, --help       show this help message and exit

Commands:
  {screenshot,ss}
    screenshot (ss)
                   Take screenshots of parts for documentation.
```

The `docs` command will:

* Remove auto-generated files such as the `_build/` and any auto-generated Sphinx sources.
* Re-generate `docs/_build/`, `docs/<base package>/`, `docs/freecad/<base package>/` by running `sphinx-build . _build` within `docs/` using the Sphinx configuration specified in `docs/conf.py`

For additional information, see [sphinx-build](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) and [Sphinx Configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html).

---

Additionally, you may pass a `screenshot` or `ss` sub-command to the `docs` command for taking screenshots of parts in a workbench:

    osewb docs ss

This will look for parts in the `<base package>/part` package of the current workbench, and save thumbnail screen shots in the `docs/_static/screenshot/` directory for each part.

### build
OSE Workbench Platform includes a `build` command for building a workbench.

    osewb build

The `build` command aggregates the following commands into one:

1. Run tests with coverage - `osewb test --coverage`
2. Lint all code - `osewb lint`
3. Ensure the documentation builds - `osewb docs`

The `build` command exits with `0` or `1` to pass or fail the build depending upon whether the above commands return non-zero exit codes.

### make
OSE Workbench Platform includes a `make` command for "making" new code.

```
$ ose make -h ↵
usage: osewb make <command>

optional arguments:
  -h, --help            show this help message and exit

Commands:
  {workbench,wb,part,model,part-feature,pf,command}
    workbench (wb)      Make Workbench
    part                Make Part class
    model               Make Model class
    part-feature (pf)   Make Part Feature creation function
    command             Make Command class
```

#### workbench
Navigate to where you want to create your new workbench. Then run:

    osewb make workbench <machine_display_name>

Where `<machine_display_name>` is the name of the machine in **Title Case**. If this contains spaces, then surround the value in double-quotes `""`.

```
$ osewb make workbench Tractor ↵
Workbench initialized in "ose-tractor-workbench" directory.

Perform the following commands to get started:

1. Change directories and initialize the git repository:

    cd ose-tractor-workbench && git init

2. Create a conda environment and activate it:

    conda env create --file environment.yml && conda activate osetractor

3. Verify your installation:

    osewb -h
```

The above examples initializes a new workbench, in a `ose-tractor-workbench` directory, with the basic structure and files needed.

```
$ tree ose-tractor-workbench --dirsfirst ↵
ose-tractor-workbench
├── docs
│   ├── conf.py
│   └── index.rst
├── freecad
│   └── osetractor
│       ├── command
│       │   ├── _add_box
│       │   │   ├── add_box_command.py
│       │   │   └── __init__.py
│       │   └── __init__.py
│       ├── icon
│       │   ├── Box.svg
│       │   └── __init__.py
│       ├── init_gui.py
│       ├── __init__.py
│       └── OSE_Tractor.py
├── osetractor
│   ├── part
│   │   ├── _box
│   │   │   ├── box.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __init__.py
├── tests
│   ├── box_test.py
│   └── __init__.py
├── CONTRIBUTING.md
├── environment.yml
├── LICENSE
├── MANIFEST.in
├── README.md
└── setup.py

10 directories, 22 files
```

For more information, see the [Pattern Catalog](https://ose-workbench-platform.readthedocs.io/en/latest/) in the docs.

![OSE Tractor Workbench](./ose-tractor-workbench.png)

#### part
Within the repository of a workbench, run the `osewb make part` command to make a new **Part Class**.

For example,

    osewb make part Box

Makes a new `Box` part class.

For more information, see [Part Classes](https://ose-workbench-platform.readthedocs.io/en/latest/pages/pattern_catalog/part_classes.html) in the docs.

#### model
Within the repository of a workbench, run the `osewb make model` command to make a new **Model Class**.

For example,

    osewb make model Box

Makes a new `BoxModel` model class.

For more information, see [Model Classes](https://ose-workbench-platform.readthedocs.io/en/latest/pages/pattern_catalog/model_classes.html) in the docs.

#### part-feature (pf)
Within the repository of a workbench, run the `osewb make part-feature` command to make a new **Part Feature creation function**.

For example,

    osewb make part-feature my_box

Makes a new `create_my_box` part feature creation function using the `MyBoxModel` class.

For more information, see [Part Feature Sub-package](https://ose-workbench-platform.readthedocs.io/en/latest/pages/pattern_catalog/workbench_package.html#part-feature-sub-package) in the docs.

#### command
Within the repository of a workbench, run the `osewb make command` command to make a new **Command Class**.

For example,

    osewb make command AddBox

Makes a new `AddBoxCommand` class.

For more information, see [Command Classes](https://ose-workbench-platform.readthedocs.io/en/latest/pages/pattern_catalog/command_classes.html) in the docs.

### browse
OSE Workbench Platform includes a `browse` covenience command for opening documentation and coverage reports in a web browser.

```
$ osewb browse -h ↵
usage: osewb browse <command>

optional arguments:
  -h, --help           show this help message and exit

Commands:
  {docs,coverage,cov}
    docs               Opens docs in web browser
    coverage (cov)     Opens coverage report in web browser
```

The `docs` command opens `docs/_build/index.html` in a web browser, while `coverage` opens `htmlcov/index.html` in a web browser.

### editor-config
OSE Workbench Platform includes an `editor-config` command for outputting recommended VS Code configuration.

```
$ osewb editor-config -h ↵
usage: osewb editor-config

optional arguments:
  -h, --help            show this help message and exit
  -m, --merge-workspace-settings
                        Merge VS Code workspace settings.
  -o, --overwrite-workspace-settings
                        Overwrite VS Code workspace settings.
```

Simply running `osewb editor-config` will output the recommended VS Code configuration settings which user's can copy-paste into their VS Code user settings, or workspace settings, `settings.json` file(s). See [User and Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings) for additional information.

The `-m` or `--merge-workspace-settings` flag will merge the current VS workspace settings into the platform's recommended settings. The platform's settings will win any collisions or merge conflicts.

The `-o` or `--overwrite-workspace-settings` flag will overwrite the current VS Code workspace settings with either the minimal-set of recommended configuration or merged settings depending upon the presence of the `-m` flag. Before overwriting, users will see a preview of the settings and must confirm overwriting in a yes or no CLI prompt.

## Contributing
See [Contributing Guidelines](./CONTRIBUTING.md).

## License
Licensed under the [GNU Lesser General Public License, version 2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html) or LGPL v2.1. See [LICENSE](./LICENSE) for details.

This is the same license as [FreeCAD](https://wiki.freecadweb.org/Licence) to ensure this code could potentially be incorporated into future FreeCAD modules or FreeCAD source itself.
