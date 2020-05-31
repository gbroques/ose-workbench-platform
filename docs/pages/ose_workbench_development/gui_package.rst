Gui Package
===========
The ``gui`` package, located within the `base package <base_package.html>`_, contains code related to the graphical user interface of FreeCAD, such as what happens when users interact with the workbench (e.g. a user clicks a button on a toolbar), or various components the user may interact with such as dialogs or panels.

.. code-block::

    gui
    ├── command/
    ├── create_part_feature/
    ├── icon/
    ├── __init__.py
    ├── <command registry>.py
    ├── <workbench>.py

Workbench Module
----------------
Every workbench will have a **workbench module** within the ``gui`` package following the pattern ``<machine>_workbench.py``.

Where ``<machine>`` is the name of the machine in **all lower-case letters**, with spaces delimited by underscores ``_``.

The workbench module contains a *single* **workbench class** that extends ``Gui.Workbench`` following the pattern ``<Machine>Workbench``, where ``<Mahcine>`` is the name of the machine in **pascal** or **UpperCamelCase**.

For example, the **workbench class** for OSE's Tractor Workbench will be located inside the ``tractor_workbench.py`` module and named ``TractorWorkbench``:

.. code-block:: python

    import FreeCAD as App
    import FreeCADGui as Gui


    class TractorWorkbench(Gui.Workbench):

        def __init__(self):
            from .icon import get_icon_path

            cls = self.__class__
            cls.MenuText = 'OSE Tractor'
            cls.ToolTip = \
                'A workbench for designing Tractor machines by Open Source Ecology'
            cls.Icon = get_icon_path('TractorWorkbenchLogo.svg')

        def Initialize(self):
            """
            Executed when FreeCAD starts
            """
            ...

        def Activated(self):
            """
            Executed when workbench is activated.
            """
            if not(App.ActiveDocument):
                App.newDocument()

        def Deactivated(self):
            """
            Executed when workbench is deactivated.
            """
            pass

        def GetClassName(self):
            return 'Gui::PythonWorkbench'

For a complete reference for the ``Gui.Workbench`` class, see `Gui::PythonWorkbench Class Reference <https://www.freecadweb.org/api/d1/d9a/classGui_1_1PythonWorkbench.html>`_.

Command Sub-package
-------------------
`Commands in FreeCAD <https://wiki.freecadweb.org/Command>`_ are executed when users perform various actions in the workbench such as clicking a button in a toolbar or selecting an option in a menu.
