from FreeCAD import Placement, Vector

from {{ base_package }}.model import {{ model }}


def create_{{ name }}(document, name):
    """
    Creates a part feature object with the given name,
    and adds it to the document.
    """
    obj = document.addObject('Part::FeaturePython', name)
    {{ model }}(obj)
    obj.ViewObject.Proxy = 0  # Mandatory unless ViewProvider is coded
    return obj
