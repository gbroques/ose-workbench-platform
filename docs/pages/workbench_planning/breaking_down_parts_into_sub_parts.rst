Breaking Down Parts Into Sub-Parts
==================================
Once the `machine is broken down into individual parts <breaking_down_a_machine_into_parts>`_, those parts can be further broken down into **sub-parts**.

Going back to the simplified part breakdown of a 3D printer as an example:

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

We may breakdown the Frame into:

* Angled Bars
* Angled Bar Connectors

.. graphviz::
   :alt: Further part breakdown of a 3D printer with Frame breakdown
   :caption: Further part breakdown of a 3D printer with Frame breakdown
   :align: center

   digraph "3D Printer Part Breakdown" {
      graph [pad="0,0.25"]
      "3D Printer" -> "Frame";
      "3D Printer" -> "X, Y, and Z Axes";
      "3D Printer" -> "Extruder";
      "3D Printer" -> "Heated Bed";
      "Frame" -> "Angled Bars";
      "Frame" -> "Angled Bar Connectors";
   }

Similarly, we could breakdown the axes, extruder, and heated bed into sub-parts.

Then, we could continue breaking down those sub-parts into sub-parts until we get to the most basic elements of the machine.

There's no real limit to how far you can breakdown a machine. It's recommneded to continue breaking down a machine for as long as it's useful and pratctical.

.. Tip:: See `Depth of Modularity <https://wiki.opensourceecology.org/wiki/Depth_of_Modularity>`_ for more information.

The amalgamation of parts and sub-parts is called an **assembly**.

Also note, there may not be a difference between a **part** and a **sub-part**.

The "part" and "sub-part" labels are contextual.

For example, the Frame is both a part in it's own right, and a sub-part of the 3D printer.
