import FreeCAD as App
import Part
from {{ cookiecutter.base_package }}.app.part import Box
from {{ cookiecutter.base_package }}.gui.icon import get_icon_path


class AddBoxCommand:
    """
    Command to add a Box.
    """

    NAME = 'AddBox'

    def Activated(self):
        document = App.ActiveDocument
        if not document:
            document = App.newDocument()
        box = Box.make()
        Part.show(box)

    def IsActive(self):
        return True

    def GetResources(self):
        return {
            'Pixmap': get_icon_path('Box.svg'),
            'MenuText': 'Add Box',
            'ToolTip': 'Add Box'
        }
