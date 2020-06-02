Breaking Down a Machine Into Parts
==================================
Every machine can be broken down into individual parts.

For example, a simplified part breakdown of a 3D printer might be:

* Frame
* X, Y, and Z Axes
* Extruder
* Heated Bed

.. graphviz::
   :alt: Simplified part breakdown of a 3D printer
   :caption: Simplified part breakdown of a 3D printer
   :align: center

   digraph "3D Printer Part Breakdown" {
      graph [pad="0,0.25"]
      "3D Printer" -> "Frame";
      "3D Printer" -> "X, Y, and Z Axes";
      "3D Printer" -> "Extruder";
      "3D Printer" -> "Heated Bed";
   }

Each of these parts usually correspond to buttons on the **main toolbar** of a workbench, and need corresponding icons.

.. figure:: /_static/3d-printer-workbench-main-toolbar-buttons.png
   :align: center

   3D Printer Workbench: Main Toolbar Buttons

Clicking one of these buttons adds the corresponding part to the user's active document in FreeCAD.

Next Step
---------
The next step in workbench planning is `breaking these parts down further <breaking_down_parts_into_sub_parts.html>`_.
