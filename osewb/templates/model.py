import Part
from osecore.app.model import Model


class {{ name }}Model(Model):

    Type = 'OSE{{ name }}'

    def __init__(self, obj):
        super({{ name }}Model, self).__init__(obj)

    def execute(self, obj):
        """
        Called on document recompute
        """
        obj.Shape = Part.makeBox(10, 10, 10)

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state
