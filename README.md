# OSE Workbench Platform
[![PyPI version](https://badge.fury.io/py/ose-workbench-platform.svg)](https://badge.fury.io/py/ose-workbench-platform)
[![Conda version](https://anaconda.org/gbroques/ose-workbench-platform/badges/version.svg)](https://anaconda.org/gbroques/ose-workbench-platform)
[![Build Status](https://travis-ci.org/gbroques/ose-workbench-platform.svg?branch=master)](https://travis-ci.org/gbroques/ose-workbench-platform)
[![Documentation Status](https://readthedocs.org/projects/ose-workbench-platform/badge/?version=latest)](https://ose-workbench-platform.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/gbroques/ose-workbench-platform/badge.svg?branch=master)](https://coveralls.io/github/gbroques/ose-workbench-platform?branch=fix-travis)

* [Introduction](#introduction)
* [Pre-Requisites](#pre-requisites)
* [Installation](#installation)
* [Virtual Development Environment](#virtual-development-environment)
* [Unit Tests](#unit-tests)
* [Documentation](#documentation)
* [Commands](#commands)
  * [env](#env)
  * [test](#test)
  * [docs](#docs)
  * [init](#init)
  * [browse](#browse)
* [Generating Code](#generating-code)
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
Install the `ose-workbench-platform` package from the `gbroques` channel in a dedicated conda environment named `osewb` (short for **O**pen **S**ource **E**cology **W**ork**B**ench): 

    conda create --name osewb --channel gbroques ose-workbench-platform

Activate your new `osewb` environment:

    conda activate osewb

Test your installation:

    osewb --help

You can deactivate this environment later by running:

    conda deactivate

## Virtual Development Environment
We use [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) to create a reproducible [virtualized OSE workbench development environment](https://en.wikipedia.org/wiki/OS-level_virtualization) with requisite dependencies for development-time tasks like running FreeCAD, executing unit tests, and generating documentation from source-code comments.

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
  {env,test,docs,init,browse}
    env                 Commands for interacting with environments
    test                Run tests in workbench
    docs                Make documentation
    init                Initialize new workbench
    browse              Commands for opening documents in a web browser
```

Each sub-command may have flags and arguments, and additional information can be discovered via `osewb <command> -h` or `--help`.

Is `osewb` too many characters to type? We recommend [aliasing](https://en.wikipedia.org/wiki/Alias_(command)) the ``osewb`` command as ``ose`` to reduce typing and increase speed even further.

### env
OSE Workbench Platform includes a `env` command to make interacting with the requisite environment for running tests and building documentation easier.

```
$ osewb env -h ↵
usage: osewb env <command>

optional arguments:
  -h, --help   show this help message and exit

Commands:
  {bootstrap}
    bootstrap  Bootstrap environment
```

In order to run the `test` and `docs` commands, you must first:

1. Create a conda environment from the `environment.yml` file located in the root of the workbench repository
2. Activate the environment with `conda activate <environment name>`
3. Bootstrap the environment with the `osewb env boostrap` command

Note, each workbench will have it's own separate environment.

Workbench environments will be named after the base package in the workbench repository (e.g. `ose3dprinter`, `osetractor`, `osepowercube`, etc.).

Some common commands relating to managing environments with `conda` are documented in the below table.

|Description|Command|
|-----------|-------|
|**Creating** the environment|`conda env create --file environment.yml`|
|**Activating** the environment|`conda activate <environment name>`|
|**Deactivating** the environment|`conda deactivate`|

Refer to the [Conda CLI reference documentation](https://docs.conda.io/projects/conda/en/latest/commands.html) for additional information.

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

### docs
OSE Workbench Platform includes a `docs` command for building the documentation of a workbench.

    osewb docs

The `docs` command will:

* Delete the `docs/_build/` directory
* Delete the `docs/<base package>/` directory
* Re-generate `docs/_build/` and `docs/<base package>/` by running `sphinx-build . _build` within `docs/` using the Sphinx configuration specified in `docs/conf.py`
* Generate property tables for each Model class in the workbench and output them as `.csv` files in `docs/property_table/`

For additional information, see [sphinx-build](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) and [Sphinx Configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html).

### init
OSE Workbench Platform includes a `init` command for initializing a new workbench.

```
$ osewb init -h ↵
usage: osewb init <machine_display_name>

positional arguments:
  machine_display_name  Name of machine in title-case. Surround in double-
                        quotes if name contains spaces (e.g. "CEB Brick
                        Press")

optional arguments:
  -h, --help            show this help message and exit
```

Navigate to where you want to initialize a directory for your new workbench. Then run:

    osewb init <machine_display_name>

Where `<machine_display_name>` is the name of the machine in **Title Case**. If this contains spaces, then surround the value in double-quotes `""`.

```
$ osewb init Tractor ↵
Workbench initialized in "ose-tractor-workbench" directory.

Next, change directories and initialize the git repository:

    cd ose-tractor-workbench && git init
```

The above examples initializes a new workbench, in a `ose-tractor-workbench` directory, with the basic structure and files needed.

```
$ tree ose-tractor-workbench --dirsfirst ↵
ose-tractor-workbench
├── docs
│   ├── _static
│   ├── _templates
│   │   ├── package.rst_t
│   │   └── toc.rst_t
│   ├── conf.py
│   ├── index.rst
│   └── requirements.txt
├── freecad
│   └── osetractor
│       ├── command
│       │   ├── add_box
│       │   │   ├── add_box_command.py
│       │   │   └── __init__.py
│       │   └── __init__.py
│       ├── icon
│       │   ├── Box.svg
│       │   └── __init__.py
│       ├── init_gui.py
│       ├── __init__.py
│       └── register_commands.py
├── osetractor
│   ├── part
│   │   ├── box
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

12 directories, 25 files
```

For more information, see the [Pattern Catalog](https://ose-workbench-platform.readthedocs.io/en/latest/) in the docs.

![OSE Tractor Workbench](./ose-tractor-workbench.png)

### browse
OSE Workbench Platform includes a `browse` covenience command for opening documentation and coverage reports in a web browser.

```
$ osewb browse -h ↵
usage: osewb browse <command>

optional arguments:
  -h, --help       show this help message and exit

Commands:
  {docs,coverage}
    docs           Opens docs in web browser
    coverage       Opens coverage report in web browser
```

The `docs` command opens `docs/_build/index.html` in a web browser, while `coverage` opens `htmlcov/index.html` in a web browser.

## Generating Code
Within the root of a workbench repository, run the `make` command.

For example,

    osewb make command AddMotor

Will generate a new `AddMotor` command class.

> **NOTE:** This idea is not yet implemented.

## Contributing
See [Contributing Guidelines](./CONTRIBUTING.md).

## License
Licensed under the [GNU Lesser General Public License, version 2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html) or LGPL v2.1. See [LICENSE](./LICENSE) for details.

This is the same license as [FreeCAD](https://wiki.freecadweb.org/Licence) to ensure this code could potentially be incorporated into future FreeCAD modules or FreeCAD source itself.
