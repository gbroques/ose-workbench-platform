# Contributing Guidelines
The following sections are meant as contributing *guidelines*, or **best-practices**. We encourage you to follow them, but your contribution may still be accepted without following them strictly.

Are you a potential first-time contributor? Look for issues tagged with <a href="https://github.com/gbroques/ose-3d-printer-workbench/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22" style="height: 20px; padding: .15em 4px; font-weight: 600; line-height: 15px; border-radius: 2px; box-shadow: inset 0 -1px 0 rgba(27,31,35,.12); font-size: 12px;background-color: #7057ff; color: white">good first issue</a>.

## Pre-Requisites
1. Install [conda](https://docs.conda.io/projects/conda/en/latest/)
2. Install [conda-build](https://docs.conda.io/projects/conda-build/en/latest/install-conda-build.html)

## Developing Locally
Create `osewb` conda environment with `freecad`:

    conda create --name osewb --channel conda-forge --yes freecad==0.19.alpha2

Activate `osewb` environment:

    conda activate osewb

Install `ose-workbench-platform`:

    pip install --editable .

Add the `$CONDA_PREFIX/lib` directory to `$PYTHONPATH` by running:

    ./post-link.sh

**Note:** This allows `FreeCAD` to be imported as a module within `python`.

Verify everything works:

    osewb test

## Code Style Guide
Code should follow the official [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

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

## Cutting Releases
A [release.bash](./release.bash) convenience script has been included in the root of the repository to make cutting releases easier.

Currently, only G Roques, the maintainer, has credentials to deploy the a release to PyPi and Anaconda Cloud.
