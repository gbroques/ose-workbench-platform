Model Classes
=============
Model classes act as extensions to `Part Classes <part_classes.html>`_, for when you want dynamic geometry, or parameteric properties the user can manipulate in FreeCAD's GUI within the `Property Editor <https://wiki.freecadweb.org/Property_editor>`_ after the part is made.

For example, extending our ``Box`` part class to make the length and width editable by the user:

.. code-block:: python

    from example.app.part import Box


    class BoxModel:

        def __init__(self, obj):
            self.Type = 'Box'

            obj.Proxy = self

            obj.addProperty('App::PropertyLength', 'Length',
                            'Dimensions', 'Box length').Length = 10.0
            obj.addProperty('App::PropertyLength', 'Width',
                            'Dimensions', 'Box width').Width = 10.0

        def execute(self, obj):
            obj.Shape = Box.make(obj.Length, obj.Width)

The constructor or ``__init__`` method initializes the parameteric properties, and the ``execute`` method handles the construction of the geometry.

For additional information, see the FreeCAD Wiki on `FeaturePython Objects <https://wiki.freecadweb.org/FeaturePython_Objects>`_ and `Scripted Objects <https://wiki.freecadweb.org/Scripted_objects>`_.
