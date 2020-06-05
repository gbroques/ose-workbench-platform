Defining Relationships Between Parts
====================================
Once the `parts are designed <designing_parts.html>`_, relationships between parts can be defined.

A common way to relate parts is through **attachment**.

For example, in a 3D Printer, axes can be attached to the frame.

If the user moves the frame, then the axes should also move accordingly.

Note, these relationships can be hierarchical.

For example, you can attach an X axis to the top of the frame.

Then, you can attach an extruder to the X axis.

The extruder isn't directly attached to the frame, but if the frame moves, then the X axis would move, and thus the extruder would also move.

It's also possible that values for parameteric properties trickle down from parts to sub-parts.

For example, the Frame can have a thickness property that adjusts how thick the metal is.

Sub-parts like the angled bars and connectors inherit the value for the thickness property of the frame to ensure they always match.
