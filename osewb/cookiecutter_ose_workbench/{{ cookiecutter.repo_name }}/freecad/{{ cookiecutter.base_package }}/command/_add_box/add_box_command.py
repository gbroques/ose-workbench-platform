import FreeCAD as App
import Part

from freecad.{{ cookiecutter.base_package }}.icon import get_icon_path
from {{ cookiecutter.base_package }}.part import Box


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
