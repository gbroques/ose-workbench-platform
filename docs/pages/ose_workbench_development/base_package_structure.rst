Base Package Structure
======================
FreeCAD is made from the beginning to work as a command-line application without its user interface.
Therefore, almost everything is separated between a "geometry" component and a "visual" component.
When you execute FreeCAD in command-line mode, the geometry part is present, but the visual part is absent.

For more information, see `"Python scripting tutorial - App and Gui", on the FreeCAD Wiki <https://wiki.freecadweb.org/Python_scripting_tutorial#App_and_Gui>`_.

OSE workbenches mirror this structure and separate the base package into two main sub-packages: ``app`` and ``gui``.

In doing so, workbenches gain the following advantages:

* Provide the ability to run the ``app`` package from a command-line context, similar to FreeCAD
* Encapsulate logic in the ``app`` package, and keep the ``gui`` package "dumb" 
* Make the ``app`` package easy to write unit tests for

At a high-level, the ``app`` package contains code related to the geometry of parts, and how those parts relate to each other.

While the ``gui`` package contains code related to the graphical user interface of FreeCAD, such as what happens when buttons are clicked, or various components the user may interact with like dialogs and panels.

Code in the ``gui`` package may reference code in the ``app`` package, while **the reverse is not true**.

The main goal of this rule is to decouple machine-specific knowledge, such as the geometry of parts, from it's graphical representation.

In doing so, other frontends besides FreeCAD's GUI can be used to display and interact with OSE's machines.
For example, imagine other desktop, web, or mobile applications.
