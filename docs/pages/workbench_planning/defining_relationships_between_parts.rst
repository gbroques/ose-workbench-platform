Defining Relationships Between Parts
====================================
Once the `parts are designed <designing_parts.html>`_, relationships between parts can be defined.

Attachment
----------
A common way to relate parts together is through **attachment**.

For example, in a 3D Printer, axes can be attached to the frame.

If the user moves the frame, then the axes should move accordingly.

Note, these relationships can be hierarchical.

For example, you can attach an X axis to the top of the frame.

Then, you can attach an extruder to the X axis.

The extruder isn't directly attached to the frame, but if the frame moves, then the X axis should move, and thus the extruder should also move.

Parent-Child Relationships
--------------------------
It's also possible that values for properties trickle down from parts to sub-parts through parent-child relationships.

For example, the 3D Printer frame may a thickness property to adjust how thick the metal is.

Sub-parts like the angled bars and connectors inherit the value for the thickness property of the frame to ensure they always match.

Identifying properties that flow from parent to child parts can be helpful prior to development.

.. Tip:: Tree diagrams can be made in the part breakdown phase to visualize parent-child part relationships