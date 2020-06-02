Root Repository Contents
========================
The following page describes the directories and files included in the root of the repository.

.. code-block::

    .
    ├── docs/
    ├── <base package>/
    ├── test/
    ├── README.md
    ├── LICENSE
    ├── CONTRIBUTING.md
    ├── InitGui.py
    ├── .readthedocs.yml
    ├── .travis.yml
    └── .gitignore

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

InitGui.py
----------
Workbenches **must** contain a ``InitGui.py`` file in the root of the repository containing code to add the workbench to FreeCAD.

.. code-block:: python

    import FreeCADGui as Gui
    from <base package>.gui import MyWorkbench

    Gui.addWorkbench(MyWorkbench())

Base Package
------------
Workbenches should have a **base package**, or directory containing all their source code named ``ose<machine>``, where ``<machine>`` is the name of the machine in all lower-case letters without spaces, hypens, or underscores.

For example, the base package of the ``ose-power-cube-workbench`` should be named ``osepowercube``.

This naming convention follows `PEP 8's guidance on package naming <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_:

    Python packages should ... have short, all-lowercase names, ... the use of underscores is discouraged.

    -- `PEP 8 <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_

For additional information, see `Base Package <base_package.html>`_.

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

.gitignore
----------
A `.gitignore file <https://git-scm.com/docs/gitignore>`_ should be included to specify any directories and files that shouldn't be checked into version control.
