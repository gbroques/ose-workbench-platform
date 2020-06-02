App Package
===========
The ``app`` package, located within the `base package <base_package.html>`_, contains code for the geometry of parts, and how those parts relate to each other.

The "geometry of parts" is defined as:

* Geometric primitives that make up parts such as vertexes, edges, and faces
* Basic shapes such as boxes, circles, cones, and cylinders
* and operations on, or between these primitives and basic shapes such as `extrusion <https://en.wikipedia.org/wiki/Extrusion>`_, `chamfer <https://en.wikipedia.org/wiki/Chamfer>`_, `union <https://en.wikipedia.org/wiki/Union_(set_theory)>`_, `difference <https://en.wikipedia.org/wiki/Complement_(set_theory)>`_, or `intersection <https://en.wikipedia.org/wiki/Intersection_(set_theory)>`_

For a formal introduction to these concepts, see `Solid modeling <https://en.wikipedia.org/wiki/Solid_modeling>`_, `Constructive solid geometry <https://en.wikipedia.org/wiki/Constructive_solid_geometry>`_, and `Boundary representation <https://en.wikipedia.org/wiki/Boundary_representation>`_.

FreeCAD exposes the ability to define and manipulate the geometry of parts through it's `Part module <https://wiki.freecadweb.org/Part_Module>`_.

See the FreeCAD Wiki on `Creating and manipulating geometry <https://wiki.freecadweb.org/Manual:Creating_and_manipulating_geometry>`_, and `Topological data scripting <https://wiki.freecadweb.org/Topological_data_scripting>`_ for additional details.

Sub-packages
------------
The following are typical sub-packages the ``app`` package may contain:

.. code-block::

    app
    ├── part/
    ├── model/
    ├── attachment/
    └── __init__.py

.. Note:: The ``app`` package typically only contains sub-packages without any direct modules.

Part Sub-package
----------------
The ``part`` sub-package exposes `Part Classes <part_classes.html>`_ encapsulating the geometry for parts, and is made up of further sub-packages for each part.

For example, the ``part`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    app/part
    ├── axis/
    ├── extruder/
    ├── frame/
    ├── heated_bed/
    └── __init__.py

The ``axis/`` package exposes an ``Axis`` class for "making" the geometry of an axis.

Similarly, the ``extruder/`` package exposes an ``Extruder`` class, ``heated_bed/`` exposes a ``HeatedBed`` class, and ``frame/`` exposes multiple classes related to a frame.

All the exposed part classes are imported within the ``__init__.py`` file:

.. code-block:: python

    from .axis import Axis
    from .extruder import Extruder
    from .frame import AngledBarFrame, AngleFrameConnector, CNCCutFrame
    from .heated_bed import HeatedBed

For more information on part classes themselves, see `Part Classes <part_classes.html>`_.

Model Sub-package
-----------------
The ``model`` sub-package exposes `Model Classes <model_classes.html>`_ for making the *static* geometry of part classes **dynamic**.

For example, the ``model`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    app/model
    ├── axis/
    ├── extruder/
    ├── frame/
    ├── heated_bed/
    └── __init__.py

The ``axis/`` package exposes an ``AxisModel`` class for "making" the geometry of the ``Axis`` part class dynamic.

Similarly, the ``extruder/`` package exposes an ``ExtruderModel`` class, ``heated_bed/`` exposes a ``HeatedBedModel`` class, and ``frame/`` exposes a ``FrameModel`` class.

All the exposed model classes are imported within the ``__init__.py`` file:

.. code-block:: python

    from .extruder import ExtruderModel
    from .frame import FrameModel
    from .heated_bed import HeatedBedModel
    from .axis import AxisModel

For more information on model classes themselves, see `Model Classes <model_classes.html>`_.

Attachment Sub-package
----------------------
The ``attachment`` sub-package exposes `Attachment Functions <attachment_functions.html>`_ that return keyword arguments to make one part appear "attached to" another.

For example, the ``attachment`` package in the ``ose-3d-printer-workbench`` contains the following:

.. code-block::

    app/attachment
    ├── get_axis_frame_attachment_kwargs/
    ├── get_extruder_axis_attachment_kwargs/
    ├── get_heated_bed_frame_axis_attachment_kwargs/
    └── __init__.py

The ``get_axis_frame_attachment_kwargs/`` package exposes an ``get_axis_frame_attachment_kwargs`` function for "attaching" the axis to the frame.

Similarly, the ``get_extruder_axis_attachment_kwargs/`` package exposes an ``get_extruder_axis_attachment_kwargs`` function, and ``get_heated_bed_frame_axis_attachment_kwargs/`` exposes a ``get_heated_bed_frame_axis_attachment_kwargs`` function.

All the exposed attachment functions are imported within the ``__init__.py`` file:

.. code-block:: python

    from .get_axis_frame_attachment_kwargs import (
        get_axis_frame_attachment_kwargs, get_default_axis_creation_kwargs)
    from .get_extruder_axis_attachment_kwargs import \
        get_extruder_axis_attachment_kwargs
    from .get_heated_bed_frame_axis_attachment_kwargs import \
        get_heated_bed_frame_axis_attachment_kwargs

For more information on attachment functions themselves, see `Attachment Functions <attachment_functions.html>`_.
