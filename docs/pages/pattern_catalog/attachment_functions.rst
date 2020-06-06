Attachment Functions
====================
.. admonition:: Motivation

   Make parts appear attached to each other.

Attachment functions return keyword arguments to make one part to appear "attached to" another.

Each attachment function is named following the pattern ``get_<attachee part>_<attached to part>_attachment_kwargs`` where:

* ``<attachee part>`` is the part being attached to another part
* and ``<attached to part>`` is the part getting attached to

Attachment functions returns a `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ ``{}``, or set of `keyword arguments <https://docs.python.org/3/glossary.html#term-argument>`_ (a.k.a "kwargs") for the *attachee part*.

The keyword arguments typically describe parameters like placement and orientation the attachee part must be in to appear "attached to" the desired part.

An Example
----------
Let's take a concrete example from the `ose-3d-printer-workbench <https://github.com/gbroques/ose-3d-printer-workbench>`_.

Consider attaching an axis to the frame in a D3D printer, and the `get_axis_frame_attachment_kwargs <https://github.com/gbroques/ose-3d-printer-workbench/tree/master/ose3dprinter/app/attachment/get_axis_frame_attachment_kwargs>`_ attachment function.

.. code-block::

    def get_axis_frame_attachment_kwargs(frame,
                                         selected_frame_face,
                                         axis_orientation):
    ...

First, let's deconstruct the name.

The *attachee part* is the **axis**, and the part getting *attached-to* is the **frame**.

The first argument to the attachment function **is always** the *attached-to* part. In this case, the ``frame``.

Other arguments will vary from attachment function to attachment function depending upon requirements, but might include selected faces, or other parts.

In this case, the second and third arguments are the face the user selected (``selected_frame_face``), and the selected orientation of the axis (``axis_orienation``).

Consider the dictionary, or axis kwargs, ``get_axis_frame_attachment_kwargs`` returns when attaching the axis to the **front face** of the frame:

.. code-block:: python

    {
        "carriage_position": 90,
        "placement": Placement [Pos=(152.4,0,0), Yaw-Pitch-Roll=(0,0,0)],
        "orientation": "z",
        "origin_translation_offset": Vector (-0.5, -1.0, 0.0),
        "length": "304.8 mm",
        "side": "front"
    }


.. figure:: /_static/attaching-z-axis-to-front-face-of-frame.png
   :align: center

   Attaching axis to front face of frame

These keyword arguments describe how to make the axis geometry appear attached to the desired position on the frame.
