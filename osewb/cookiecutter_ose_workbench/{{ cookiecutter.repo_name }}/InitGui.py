import FreeCADGui as Gui
from {{ cookiecutter.base_package }}.gui import {{ cookiecutter.workbench_class_name }}

Gui.addWorkbench({{ cookiecutter.workbench_class_name }}())
