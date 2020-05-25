import FreeCAD as App
import FreeCADGui as Gui


class {{ cookiecutter.workbench_class_name }}(Gui.Workbench):
    """
    {{ cookiecutter.machine_display_name }} Workbench
    """

    def __init__(self):
        from .icon import get_icon_path

        cls = self.__class__
        cls.MenuText = '{{ cookiecutter.machine_title }}'
        cls.ToolTip = \
            'A workbench for designing {{ cookiecutter.machine_display_name }} machines by Open Source Ecology'
        cls.Icon = get_icon_path('Box.svg')

    def Initialize(self):
        """
        Executed when FreeCAD starts
        """
        from importlib import import_module
        command_registry = import_module(
            '.{{ cookiecutter.command_registry_filename }}', package='{{ cookiecutter.base_package }}.gui')

        main_toolbar, main_menu = command_registry.register_commands()

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
