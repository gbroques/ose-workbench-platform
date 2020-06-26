"""Imported when FreeCAD starts up to add workbench to GUI."""
import FreeCAD as App
import FreeCADGui as Gui

from .icon import get_icon_path
from .{{ cookiecutter.command_registry_filename }} import register_commands


class {{ cookiecutter.workbench_class_name }}(Gui.Workbench):
    """
    {{ cookiecutter.machine_display_name }} Workbench
    """
    MenuText = '{{ cookiecutter.machine_title }}'
    ToolTip = \
        'A workbench for designing {{ cookiecutter.machine_display_name }} machines by Open Source Ecology'
    Icon = get_icon_path('Box.svg')

    def Initialize(self):
        """
        Executed when FreeCAD starts
        """
        main_toolbar, main_menu = register_commands()

        self.appendToolbar('{{ cookiecutter.machine_title }}', main_toolbar)
        self.appendMenu('{{ cookiecutter.machine_title }}', main_menu)

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


Gui.addWorkbench({{ cookiecutter.workbench_class_name }}())
