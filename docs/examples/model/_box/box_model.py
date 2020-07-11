import Part


class BoxModel:
    """
    Encapsulates the data (i.e. topography and shape) for a Box,
    and is separate from the "view" or GUI representation.
    """

    def __init__(self, obj):
        self.Type = 'Box'

        obj.Proxy = self
        obj.addProperty('App::PropertyLength', 'Length',
                        'Dimensions', 'Box length').Length = 10.0
        obj.addProperty('App::PropertyLength', 'Width',
                        'Dimensions', 'Box width').Width = 10.0
        obj.addProperty('App::PropertyLength', 'Height',
                        'Dimensions', 'Box height').Height = 10.0

    def execute(self, obj):
        obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)
