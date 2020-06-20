Root Repository Contents
========================
.. admonition:: Motivation

   Ensure workbenches contain the same core elements.

The following page describes the directories and files included in the root of the repository.

.. code-block::

    $ tree -a --sort=name -L 1 -F --dirsfirst ↵
    .
    ├── docs/
    ├── freecad/<package name>/
    ├── <package name>/
    ├── tests/
    ├── CONTRIBUTING.md
    ├── environment.yml
    ├── .gitignore
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.md
    ├── .readthedocs.yml
    └── setup.py

README File
-----------
Every workbench should have a `README file <https://en.wikipedia.org/wiki/README>`_, named ``README.md``, containing basic information about the project.

License File
------------
Each workbench should include a `software license <https://en.wikipedia.org/wiki/Software_license>`_ in a file named ``LICENSE``.

We recommend the `GNU Lesser General Public License, version 2.1 <https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html>`_, as it's same license as `FreeCAD <https://wiki.freecadweb.org/Licence>`_ to ensure workbenches could potentially be incorporated into future FreeCAD modules or FreeCAD source itself.

Contributing Guidlines
----------------------
OSE workbenches should include `contributing guidelines <https://help.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors>`_ describing how people can contribute to the project inside a file named ``CONTRIBUTING.md``.

Library & Workbench Package
---------------------------
Workbenches should organize source code into two main packages:

1. A library package
2. and a workbench package

The library package should be named ``ose<machine>``, where ``<machine>`` is the name of the machine in all lower-case letters without spaces, hypens, or underscores.

The workbench package should be named the same as the library package, but located inside a directory named ``freecad/``.

For example, the library package of the ``ose-power-cube-workbench`` should be named ``osepowercube``.

.. code-block::

    .
    ├── osepowercube/          # Library Package
    └── freecad/osepowercube/  # Workbench Package

This naming convention follows `PEP 8's guidance on package naming <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_:

    Python packages should ... have short, all-lowercase names, ... the use of underscores is discouraged.

    -- `PEP 8 <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_

For additional information, see `App Gui Architecture <app_gui_architecture.html>`_.

Documentation
-------------
Documentation for workbenches should be located in the ``docs/`` directory.

Hosting of documentation should be performed by `Read the Docs <https://readthedocs.org/>`_ with configuration located in ``.readthedocs.yml``.

Tests
-----
Tests for workbenches should be located in the ``test/`` directory.

Continuous Integration
----------------------
Workbenches should use `Travis CI <https://travis-ci.org/>`_ for `Continuous Integration (CI) <https://en.wikipedia.org/wiki/Continuous_integration>`_.

Following the `Feature Branch Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow>`_, each feature branch will be tested to ensure it doesn't break existing code before that branch is merged into the ``master`` branch.

Configuration for Travis CI is located within a file named ``.travis.yml``.

Setup Module
------------
Workbenches should include a ``setup.py`` module for describing how to package and distribute the workbench as a Python package.

MANIFEST.in
-----------
The ``MANIFEST.in`` file describes additional files to include in the Python package distribution.

For more information, see `Including files in source distributions with MANIFEST.in <https://packaging.python.org/guides/using-manifest-in/>`_.

environment.yml
---------------
The ``environment.yml`` file describes how to create a conda environment for local workbench development.

.gitignore
----------
A `.gitignore file <https://git-scm.com/docs/gitignore>`_ should be included to specify any directories and files that shouldn't be checked into version control.
