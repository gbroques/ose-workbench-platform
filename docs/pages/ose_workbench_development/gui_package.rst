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
The ``command`` sub-package exposes `Command Classes <command_classes.html>`_  that are executed when users perform various actions in the workbench such as clicking a button in a toolbar or selecting an option in a menu.

For example, the ``command`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    gui/command
    ├── add_axis/
    ├── add_extruder/
    ├── add_frame/
    ├── add_heated_bed/
    ├── __init__.py

The ``add_axis/`` package exposes an ``AddAxisCommand`` that's executed when the user wants to add an axis to the document.

Similarly, the ``add_extruder/`` package exposes an ``AddExtruderCommand`` class, ``add_frame/`` exposes ``AddFrameCommand``, and ``heated_bed/`` exposes ``AddHeatedBed``.

For more information on command classes themselves, see `Command Classes <command_classes.html>`_.

Command Registry Module
-----------------------
Every workbench contains a **command registry module** within the ``gui`` package.

The command registry module is where all commands are imported, registered via ``Gui.addCommand``, and associated together into lists for adding to toolbars or menus.

The command registry module name follows the pattern ``OSE-<Machine>.py``, where ``<Machine>`` is the name of the machine, with spaces delimited by dashes ``-``.

For example, the command registry module name for the 3D Printer workbench is named ``OSE-3D-Printer.py``.

Normally python modules use all lower-case letters, and underscores ``_`` to delimit spaces, so why the deviation?

FreeCAD derives a "Category" to organize commands from the name of the Python module where ``Gui.addCommand`` is called.

Since all commands in the workbench are registered with ``Gui.addCommand`` in a Python module called ``OSE-3D-Printer.py``, the derived "Category" for grouping these commands is "OSE-3D-Printer".

We use dashes to be consistent with other command categories like ``Standard-View`` and ``Standard-Test``.

.. image:: /_static/commands.png

When you register custom commands for an external workbench via ``Gui.addCommand(commandName, commandObject)``, FreeCAD adds the command to it's global command registry.

To avoid name collisions and ensure uniqueness, a command name is typically prefixed with the name of the module and underscore. For example, "Part_Cylinder" or "OSE3DP_AddFrame".

The command registry module handles prefixing a unique namespace to the name of your command for you.

In this way, if in the future we need to change the name of our command namespace (e.g. "OSE3DP") because it collides with another external workbench, then the change is easy.

You can see a simple and relatively complete command registry module example based on the ``ose-3d-printer-workbench`` below:

.. code-block:: python

    import FreeCADGui as Gui

    from .command.add_extruder import AddExtruderCommand
    from .command.add_frame import AddFrameCommand
    from .command.add_heated_bed import AddHeatedBedCommand

    #: Command Namespace: Must be unique to all FreeCAD workbenches.
    command_namespace = 'OSE3DP'


    def register_commands():
        """
        Register all workbench commands,
        and associate them to toolbars, menus, sub-menus, and context menu.
        """
        add_frame_key = register(AddFrameCommand.NAME, AddFrameCommand())
        add_heated_bed_key = register(
            AddHeatedBedCommand.NAME, AddHeatedBedCommand())
        add_extruder_key = register(AddExtruderCommand.NAME, AddExtruderCommand())

        #: Main Toolbar Commands
        main_toolbar_commands = [
            add_frame_key,
            add_heated_bed_key,
            add_extruder_key
        ]
        return main_toolbar_commands


    def register(name, command):
        """Register a command via Gui.addCommand.

        FreeCAD uses the filename where Gui.addCommand is executed as a category
        to group commands together in it's UI.
        """
        key = from_command_name_to_key(name)
        Gui.addCommand(key, command)
        return key


    def from_command_name_to_key(command_name):
        return '{}_{}'.format(command_namespace, command_name)
