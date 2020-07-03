Library Package
===============
.. admonition:: Motivation

   Organize code related to the geometry parts, and allow parts to be made from a command-line context. 

The library package, located within the root level of the repository, contains code for the geometry of parts, and how those parts relate to each other.

The "geometry of parts" is defined as:

* Geometric primitives that make up parts such as vertexes, edges, and faces
* Basic shapes such as boxes, circles, cones, and cylinders
* and operations on, or between these primitives and basic shapes such as `extrusion <https://en.wikipedia.org/wiki/Extrusion>`_, `chamfer <https://en.wikipedia.org/wiki/Chamfer>`_, `union <https://en.wikipedia.org/wiki/Union_(set_theory)>`_, `difference <https://en.wikipedia.org/wiki/Complement_(set_theory)>`_, or `intersection <https://en.wikipedia.org/wiki/Intersection_(set_theory)>`_.

For a formal introduction to these concepts, see `Solid modeling <https://en.wikipedia.org/wiki/Solid_modeling>`_, `Constructive solid geometry <https://en.wikipedia.org/wiki/Constructive_solid_geometry>`_, and `Boundary representation <https://en.wikipedia.org/wiki/Boundary_representation>`_.

FreeCAD exposes the ability to define and manipulate the geometry of parts through it's `Part module <https://wiki.freecadweb.org/Part_Module>`_.

See the FreeCAD Wiki on `Creating and manipulating geometry <https://wiki.freecadweb.org/Manual:Creating_and_manipulating_geometry>`_, and `Topological data scripting <https://wiki.freecadweb.org/Topological_data_scripting>`_ for additional details.

Sub-packages
------------
The following are typical sub-packages the library package may contain:

.. code-block::

    <library package>/
    ├── part/
    ├── model/
    ├── attachment/
    └── __init__.py

.. Note:: The library package typically only contains sub-packages without any direct modules.

Part Sub-package
----------------
The ``part`` sub-package exposes `Part Classes <part_classes.html>`_ encapsulating the geometry for parts, and is made up of further **private** sub-packages for each part.

For example, the ``part`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    <library package>/part/
    ├── _axis/
    ├── _extruder/
    ├── _frame/
    ├── _heated_bed/
    └── __init__.py

The ``_axis/`` package exposes an ``Axis`` class for "making" the geometry of an axis.

Similarly, the ``_extruder/`` package exposes an ``Extruder`` class, ``_heated_bed/`` exposes a ``HeatedBed`` class, and ``_frame/`` exposes multiple classes related to a frame.

All the exposed part classes are imported within the ``__init__.py`` file, and declared **public** using ``__all__``:

.. code-block:: python

    """Parts for a 3D Printer."""
    from ._axis import Axis
    from ._extruder import Extruder
    from ._frame import AngledBarFrame, AngleFrameConnector, CNCCutFrame
    from ._heated_bed import HeatedBed

    __all__ = [
        'AngleFrameConnector',
        'AngledBarFrame',
        'Axis',
        'CNCCutFrame',
        'Extruder',
        'HeatedBed'
    ]

.. Tip:: It's best-practice to include docstring for all public packages.

For more information on part classes themselves, see `Part Classes <part_classes.html>`_.

Model Sub-package
-----------------
The ``model`` sub-package exposes `Model Classes <model_classes.html>`_ for making the *static* geometry of part classes **dynamic**.

For example, the ``model`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    <library package>/model
    ├── _axis/
    ├── _extruder/
    ├── _frame/
    ├── _heated_bed/
    └── __init__.py

The ``_axis/`` package exposes an ``AxisModel`` class for "making" the geometry of the ``Axis`` part class dynamic.

Similarly, the ``_extruder/`` package exposes an ``ExtruderModel`` class, ``_heated_bed/`` exposes a ``HeatedBedModel`` class, and ``_frame/`` exposes a ``FrameModel`` class.

All the exposed model classes are imported within the ``__init__.py`` file, and declared **public** using ``__all__``:

.. code-block:: python

    """Models for 3D Printer parts."""
    from ._axis import AxisModel
    from ._extruder import ExtruderModel
    from ._frame import FrameModel
    from ._heated_bed import HeatedBedModel

    __all__ = [
        'AxisModel',
        'ExtruderModel',
        'FrameModel',
        'HeatedBedModel'
    ]

For more information on model classes themselves, see `Model Classes <model_classes.html>`_.

Attachment Sub-package
----------------------
The ``attachment`` sub-package exposes `Attachment Functions <attachment_functions.html>`_ that return keyword arguments to make one part appear "attached to" another.

For example, the ``attachment`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    <library package>/attachment
    ├── _get_axis_frame_attachment_kwargs/
    ├── _get_extruder_axis_attachment_kwargs/
    ├── _get_heated_bed_frame_axis_attachment_kwargs/
    └── __init__.py

The ``_get_axis_frame_attachment_kwargs/`` package exposes an ``_get_axis_frame_attachment_kwargs`` function for "attaching" the axis to the frame.

Similarly, the ``_get_extruder_axis_attachment_kwargs/`` package exposes a ``get_extruder_axis_attachment_kwargs`` function, and ``_get_heated_bed_frame_axis_attachment_kwargs/`` exposes a ``get_heated_bed_frame_axis_attachment_kwargs`` function.

All the exposed attachment functions are imported within the ``__init__.py`` file, and declared **public** using ``__all__``:

.. code-block:: python

    """Attachment functions to make 3D Printer parts appear attached to each other."""
    from ._get_axis_frame_attachment_kwargs import (
        get_axis_frame_attachment_kwargs, get_default_axis_creation_kwargs)
    from ._get_extruder_axis_attachment_kwargs import \
        get_extruder_axis_attachment_kwargs
    from ._get_heated_bed_frame_axis_attachment_kwargs import \
        get_heated_bed_frame_axis_attachment_kwargs

    __all__ = [
        'get_axis_frame_attachment_kwargs',
        'get_default_axis_creation_kwargs',
        'get_extruder_axis_attachment_kwargs',
        'get_heated_bed_frame_axis_attachment_kwargs'
    ]

For more information on attachment functions themselves, see `Attachment Functions <attachment_functions.html>`_.
