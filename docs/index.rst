OSE Workbench Platform Documenation
===================================
A platform for workbench development by `Open Source Ecology <https://www.opensourceecology.org/>`_.

OSE defines a "workbench" as a set of tools in CAD software to design and make a particular machine.

The below **Workbench Planning** pages cover planning for workbench development.
Note, anyone can contribute to the workbench planning process, and you don't need to be a programmer.
Indeed, OSE workbench development teams benefit from a diversity of people with different backgrounds and skill-sets.

The below **Workbench Development** pages describe the standards and guidelines for implementing workbenches using the FreeCAD platform, including structure, patterns for solving common problems, branching and workflow strategy, and versioning.
Every workbench should follow these standards and guidelines to make working between various workbenches easier, and increase collaboration.

.. toctree::
   :maxdepth: 1
   :caption: Workbench Planning

   pages/workbench_planning/deciding_on_a_machine
   pages/workbench_planning/breaking_down_a_machine_into_parts
   pages/workbench_planning/designing_icons
   pages/workbench_planning/breaking_down_parts_into_sub_parts

.. toctree::
   :maxdepth: 1
   :caption: Workbench Development

   pages/workbench_development/repository_scope_and_naming
   pages/workbench_development/root_repository_contents
   pages/workbench_development/base_package
   pages/workbench_development/app_package
   pages/workbench_development/part_classes
   pages/workbench_development/model_classes
   pages/workbench_development/attachment_functions
   pages/workbench_development/gui_package
   pages/workbench_development/command_classes
   pages/workbench_development/branching_and_workflow_strategy
   pages/workbench_development/versioning

.. toctree::
   :maxdepth: 1
   :caption: osewb package

   osewb/osewb

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
