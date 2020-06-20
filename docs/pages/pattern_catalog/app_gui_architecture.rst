App Gui Architecture
====================
.. admonition:: Motivation

   Encapsulate source code and separate the geometry of parts from their graphical representation.

FreeCAD is made from the beginning to work as a command-line application without its user interface.
Therefore, almost everything is separated between a "geometry" component and a "visual" component.
When you execute FreeCAD in command-line mode, the geometry part is present, but the visual part is absent.

For more information, see `"Python scripting tutorial - App and Gui", on the FreeCAD Wiki <https://wiki.freecadweb.org/Python_scripting_tutorial#App_and_Gui>`_.

OSE workbenches mirror this structure, and separate code into two main sub-packages:

1. A library package containing ``App`` functionality
2. A workbench package containing ``Gui`` functionality

In doing so, workbenches gain the following advantages:

* Provide the ability to run the library package from a command-line context, similar to FreeCAD
* Encapsulate logic in the library package, and keep the workbench package "dumb" 
* Make the library package easy to write unit tests for

At a high-level, the library package contains code related to the geometry of parts, and how those parts relate to each other.

While the workbench package contains code related to the graphical user interface of FreeCAD, such as what happens when users interact with the workbench (e.g. a user clicks a button on a toolbar), or various components the user may interact with such as dialogs or panels.

Code in the workbench package may reference code in the library package, while **the reverse is not true**.

The main goal of this rule is to decouple machine-specific knowledge, such as the geometry of parts, from it's graphical representation.

In doing so, theoretically, other frontends besides FreeCAD's GUI can be used to display and interact with OSE's machines.
For example, imagine other desktop, web, or mobile applications.

See `Library Package <library_package.html>`_ and `Workbench Package <workbench_package.html>`_ for additional information.
