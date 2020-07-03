Command Classes
===============
.. admonition:: Motivation

   Encapsulate action users can perform when interacting with FreeCAD's UI.

Command Classes are executed when users perform various actions in the workbench such as clicking a button in a toolbar or selecting an option in a menu.

OSE Workbench Command Classes are an opinionated extension to `FreeCAD Command Classes <https://wiki.freecadweb.org/Command>`_ with the following observed conventions:

1. Names sound like actions, typically begin with verbs, and always end with a "command" suffix

    * For example, a command class to add a frame to the document might be named ``AddFrameCommand``
    * The command should be located in a module named after the command (e.g. ``add_frame_command.py``)

2. Have a static ``NAME`` **string** constant

    * Typically the same name as the command (e.g. ``'AddFrameCommand'``)

.. Important:: ``NAME`` must be unique for all commands within the scope of the workbench

3. Located and exposed by the ``command`` sub-package of the `workbench package <workbench_package.html>`_.

.. code-block::

    freecad/ose3dprinter/command
    ├── _add_frame/
    │   ├── add_frame_command.py
    │   └── __init__.py
    └── __init__.py

Within ``_add_frame/__init__.py``:

.. code-block:: python

    from .add_frame_command import AddFrameCommand

    __all__ = ['AddFrameCommand']

Within ``freecad/ose3dprinter/command/__init__.py``:

.. code-block:: python

    """Commands users can perform in FreeCAD's GUI."""
    from ._add_frame import AddFrameCommand

    __all__ = ['AddFrameCommand',]

The following is a complete example taken from the `ose-3d-printer-workbench <https://github.com/gbroques/ose-3d-printer-workbench/tree/master/ose3dprinter/gui/command/add_frame>`_:

.. code-block::

    import FreeCAD as App

    from freecad.ose3dprinter.icon import get_icon_path
    from freecad.ose3dprinter.part_feature import create_frame


    class AddFrameCommand:
        """
        Command to add Frame object.
        """

        NAME = 'AddFrame'

        def Activated(self):
            document = App.ActiveDocument
            if not document:
                document = App.newDocument()
            create_frame(document, 'Frame')
            document.recompute()

        def IsActive(self):
            return True

        def GetResources(self):
            return {
                'Pixmap': get_icon_path('Frame.svg'),
                'MenuText': 'Add Frame',
                'ToolTip': 'Add Frame'
            }

For additional information, see `Command <https://wiki.freecadweb.org/Command>`_ on the FreeCAD Wiki.
