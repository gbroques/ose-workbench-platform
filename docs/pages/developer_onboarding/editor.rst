Editor
======
The following page outlines guides for recommended editors and integrated development environments (IDEs) for OSE workbench development.

Visual Studio Code |VS Code logo|
---------------------------------
`Visual Studio Code <https://code.visualstudio.com/>`_ is a **free**, cross-platform, extensible editor built on open-source.

.. |VS Code logo| image:: /_static/vscode.svg
   :alt: VS Code logo
   :width: 24px

Recommended Extensions
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
    :header-rows: 1

    * - Extension
      - Description
    * - `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
      - Python language support
    * - `Python Test Explorer for Visual Studio Code <https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter>`_
      - Run your Python Unittest or Pytest tests with the `Test Explorer UI <https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer>`_.
    * - `Python Docstring Generator <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_
      - Quickly generate docstrings for python functions.

Recommended Extensions Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OSE Workbench Platform includes an ``editor-config`` command configuring the above VS Code extensions with the recommended configuration.

See the `editor-config command documentation in the README <https://github.com/gbroques/ose-workbench-platform#editor-config>`_ for additional information.

.. include:: ../../../README.md
   :literal:
   :start-after: ### editor-config
   :end-before: ## Contributing

Python Docstring Generator Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A **custom docstring template** for OSE workbenches has been included in ``ose-workbench-platform/osewb/.mustache``.

.. include:: ../../../osewb/.mustache
   :literal:

You should configure the extension to use this template in order to avoid adding **types** to your docstrings.

Types in docstrings are redundant with `Type Hints <https://www.python.org/dev/peps/pep-0484/>`_ — the preferred way to document the types in Python.

.. admonition:: Is VS Code open-source?

   `Explained by a VS Code developer <https://github.com/Microsoft/vscode/issues/60#issuecomment-161792005>`_:

      When we set out to open source our code base, we looked for common practices to emulate for our scenario. We wanted to deliver a Microsoft branded product, built on top of an open source code base that the community could explore and contribute to.
      
      We observed a number of branded products being released under a custom product license, while making the underlying source code available to the community under an open source license. For example, Chrome is built on Chromium, the Oracle JDK is built from OpenJDK [...] Those branded products come with their own custom license terms, but are built on top of a code base that’s been open sourced.
      
      We then follow a similar model for Visual Studio Code. We build on top of the vscode code base we just open sourced and we release it under a standard, pre-release Microsoft license.

VSCodium
--------
For open-source purists, you may be interested in the MIT-licensed `VSCodium <https://vscodium.com/>`_ as a VS Code alternative.
