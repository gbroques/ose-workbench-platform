OSE Workbench Platform Documentation
====================================
A platform for workbench development by `Open Source Ecology <https://www.opensourceecology.org/>`_.

OSE defines a "workbench" as a set of tools in CAD software to design and make a particular machine.

The below **Workbench Planning** pages cover planning for workbench development.
Note, anyone can contribute to the workbench planning process, and you don't need to be a programmer.
Indeed, OSE workbench development teams benefit from a diversity of people with different backgrounds and skill-sets.

The below **Developer Onboarding** pages contain guides for getting setup as an OSE workbench developer.

The below **Development Process** pages describe various processes related to development such as breaking down development work, branching, and versioning.

The below **Pattern Catalog** pages describe structure and patterns for solving common problems in workbenches using the FreeCAD platform.

Every workbench should follow the above standards and guidelines to make working between various workbenches easier, and increase collaboration.

.. toctree::
   :maxdepth: 1
   :caption: Workbench Planning

   pages/workbench_planning/deciding_on_a_machine
   pages/workbench_planning/breaking_down_a_machine_into_parts
   pages/workbench_planning/designing_icons
   pages/workbench_planning/breaking_down_parts_into_sub_parts
   pages/workbench_planning/designing_parts
   pages/workbench_planning/defining_relationships_between_parts


.. toctree::
   :maxdepth: 1
   :caption: Developer Onboarding

   pages/developer_onboarding/editor


.. toctree::
   :maxdepth: 1
   :caption: Development Process

   pages/development_process/breakdown_strategy
   pages/development_process/branching_strategy
   pages/development_process/versioning_strategy
   pages/development_process/third_party_services

.. toctree::
   :maxdepth: 1
   :caption: Pattern Catalog

   pages/pattern_catalog/repository_scope_and_naming
   pages/pattern_catalog/root_repository_contents
   pages/pattern_catalog/app_gui_architecture
   pages/pattern_catalog/library_package
   pages/pattern_catalog/part_classes
   pages/pattern_catalog/model_classes
   pages/pattern_catalog/attachment_functions
   pages/pattern_catalog/workbench_package
   pages/pattern_catalog/command_classes

.. toctree::
   :maxdepth: 1
   :caption: OSE Workbench Ecosystem

   pages/ose_workbench_ecosystem/ose_workbench_ecosystem

.. toctree::
   :maxdepth: 1
   :caption: osewb package

   osewb/osewb

.. toctree::
   :maxdepth: 1
   :caption: osewb.doc.ext examples

   osewb/examples/examples

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
