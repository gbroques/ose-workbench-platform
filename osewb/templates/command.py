import FreeCAD as App

from freecad.{{ base_package }}.icon import get_icon_path


class {{ name }}Command:
    """TODO: Fill in the blank: Command to ____."""

    NAME = '{{ name }}'

    def Activated(self):
        document = App.ActiveDocument
        if not document:
            document = App.newDocument()
        # TODO: Create some part
        document.recompute()

    def IsActive(self):
        return True

    def GetResources(self):
        # TODO: Fill-in icon name, MenuText, and ToolTip
        return {
            'Pixmap': get_icon_path(''),
            'MenuText': '',
            'ToolTip': ''
        }
