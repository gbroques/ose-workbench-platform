Workbench Package
=================
.. admonition:: Motivation

   Organize code related to the graphical representation of parts and a workbench.

The workbench package, located within the ``freecad/`` directory, contains code related to the graphical user interface of FreeCAD, such as what happens when users interact with the workbench (e.g. a user clicks a button on a toolbar), or various components the user may interact with such as dialogs or panels.

.. code-block::

    freecad/<workbench package>/
    ├── command/
    ├── icon/
    ├── part_feature/
    ├── __init__.py
    ├── init_gui.py
    └── register_commands.py

init_gui.py
-----------
Every workbench will have a ``init_gui.py`` module within the workbench package.

The ``init_gui.py`` module contains a *single* **workbench class** that extends ``Gui.Workbench`` following the pattern ``<Machine>Workbench``, where ``<Mahcine>`` is the name of the machine in **pascal** or **UpperCamelCase**.

For example, the **workbench class** for OSE's Tractor Workbench will be located inside the ``init_gui.py`` module and named ``TractorWorkbench``:

.. code-block:: python

    import FreeCAD as App
    import FreeCADGui as Gui

    from .icon import get_icon_path
    from .register_commands import register_commands


    class TractorWorkbench(Gui.Workbench):
        """
        Tractor Workbench
        """
        MenuText = 'OSE Tractor'
        ToolTip = \
            'A workbench for designing Tractor machines by Open Source Ecology'
        Icon = get_icon_path('Tractor.svg')

        def Initialize(self):
            """
            Executed when FreeCAD starts
            """
            main_toolbar, main_menu = register_commands()

            self.appendToolbar('OSE Tractor', main_toolbar)
            self.appendMenu('OSE Tractor', main_menu)

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


    Gui.addWorkbench(TractorWorkbench())

.. Important:: FreeCAD imports this module when it initializes it's GUI. The last statement in ``init_gui.py`` instantiates the **workbench class** and adds it to FreeCAD via ``Gui.addWorkbench``.

For a complete reference of the ``Gui.Workbench`` class, see `Gui::PythonWorkbench Class Reference <https://www.freecadweb.org/api/d1/d9a/classGui_1_1PythonWorkbench.html>`_.

Command Sub-package
-------------------
The ``command`` sub-package exposes `Command Classes <command_classes.html>`_  that are executed when users perform various actions in the workbench such as clicking a button in a toolbar or selecting an option in a menu.

For example, the ``command`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    freecad/<workbench package>/command
    ├── add_axis/
    ├── add_extruder/
    ├── add_frame/
    ├── add_heated_bed/
    └── __init__.py

The ``add_axis/`` package exposes an ``AddAxisCommand`` that's executed when the user wants to add an axis to the document.

Similarly, the ``add_extruder/`` package exposes an ``AddExtruderCommand`` class, ``add_frame/`` exposes ``AddFrameCommand``, and ``heated_bed/`` exposes ``AddHeatedBed``.

For more information on command classes themselves, see `Command Classes <command_classes.html>`_.

Command Registry Module
-----------------------
Every workbench contains a **command registry module** within the workbench package.

The command registry module is where all commands are imported, registered via ``Gui.addCommand``, and associated together into lists for adding to toolbars or menus.

The command registry module name follows the pattern ``OSE_<Machine>.py``, where ``<Machine>`` is the name of the machine, with spaces delimited by underscores ``_``.

For example, the command registry module name for the 3D Printer workbench is named ``OSE_3D_Printer.py``.

Normally python modules use all lower-case letters, so why the deviation?

FreeCAD derives a "Category" to organize commands from the name of the Python module where ``Gui.addCommand`` is called.

Since all commands in the workbench are registered with ``Gui.addCommand`` in a Python module called ``OSE_3D_Printer.py``, the derived "Category" for grouping these commands is "OSE_3D_Printer".

.. image:: /_static/commands.png
   :alt: Available commands in FreeCAD grouped together by categories

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
        add_frame_key = _register(AddFrameCommand.NAME, AddFrameCommand())
        add_heated_bed_key = _register(
            AddHeatedBedCommand.NAME, AddHeatedBedCommand())
        add_extruder_key = _register(AddExtruderCommand.NAME, AddExtruderCommand())

        #: Main Toolbar Commands
        main_toolbar_commands = [
            add_frame_key,
            add_heated_bed_key,
            add_extruder_key
        ]
        return main_toolbar_commands


    def _register(name, command):
        key = '{}_{}'.format(command_namespace, name)
        Gui.addCommand(key, command)
        return key


Icon Sub-package
----------------
The ``icon`` sub-package contains icons for the workbench (typically in ``.svg`` format) and exposes a ``get_icon_path`` function that takes the name of an icon file and returns the absolute path to the icon.

.. code-block:: python

    from .icon import get_icon_path

    get_icon_path('MyIcon.svg') # => /home/user/.FreeCAD/Mod/my-workbench/myworkbench/gui/icon/MyIcon.svg


Part Feature Sub-package
------------------------
The ``part_feature`` sub-package exposes functions to create `Part Feature objects <https://wiki.freecadweb.org/Part_Feature>`_.

For example, the ``part_feature`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    freecad/<workbench package>/part_feature
    ├── axis/
    ├── extruder/
    ├── frame/
    ├── heated_bed/
    └── __init__.py

The ``axis/`` package exposes a ``create_axis`` function that creates and adds an axis part feature object to a specified document.

Similarly, the ``extruder/`` package exposes a ``create_extruder`` function, ``frame/`` exposes ``create_frame``, and ``heated_bed/`` exposes ``create_heated_bed``.

A simple example of a part feature creation function looks like:

.. code-block:: python

    from ose3dprinter.app.model import AxisModel


    def create_axis(document, name):
        """
        Creates a axis object with the given name,
        and adds it to a document.
        """
        obj = document.addObject('Part::FeaturePython', name)
        AxisModel(obj)
        obj.ViewObject.Proxy = 0  # Mandatory unless ViewProvider is coded
        return obj

The single responsibility of a part feature creation function is to add a ``Part::FeaturePython`` to a document, and decorate it with a model class, and *optionally* a `view provider <https://wiki.freecadweb.org/Viewprovider>`_.
