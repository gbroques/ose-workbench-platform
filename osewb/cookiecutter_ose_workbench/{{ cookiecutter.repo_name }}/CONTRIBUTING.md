# Contributing Guidelines
The following sections are meant as contributing *guidelines*, or **best-practices**. You're encouraged to follow them, but contributions may still be accepted without following them strictly.

## Pre-Requisites
Create a conda environment:

    conda env create --file environment.yml

Active environment:

    conda activate {{ cookiecutter.base_package }}

Bootstrap activated environment:

    osewb env bootstrap

## Code Style Guide
Code should follow the official [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

## Tests
Unit tests are encouraged for complex non-trivial logic (e.g. attaching axes to the frame), and can be found in the `tests/` directory within the root of this repository.

It's expected that you fix any changes you make that break existing tests.

Pull requests will not be merged if tests are failing.

To execute all unit tests, run:

    osewb test

## Documentation
Improving the docstring on packages, modules, classes, functions, and other symbols throughout the codebase is encouraged.

We use the [Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) which is the standard docstring format used with [Sphinx](https://www.sphinx-doc.org/en/master/).

To build the docs, run:

    osewb docs

## Philosophy
We generally subscribe to the philosophy provided by [The Zen of Python](https://www.python.org/dev/peps/pep-0020/).

```
>>> import this;
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
