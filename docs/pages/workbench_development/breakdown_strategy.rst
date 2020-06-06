Breakdown Strategy
==================
This page defines a process for breaking down the development work of a workbench.

1. Initialize Workbench
2. Make Parts
3. Parameterize Parts
4. Attachment
5. Cut List Generation
6. CAM File Generation

If you have multiple developers, then work on separate parts in parallel:

.. graphviz::
   :alt: Breakdown Strategy for Multiple Developers
   :caption: Breakdown Strategy for Multiple Developers
   :align: center

    digraph verticalslices {
        subgraph cluster_0 {
            style=filled;
            color="#e3e3e3";
            node [style=filled,color=white];
            "Make Axis" -> "Parameterize Axis" -> "Add Axis to Cut List" -> "Make Axis CAM";
            label = "Developer 1";
        }

        subgraph cluster_1 {
            node [style=filled,color="#e3e3e3"];
            "Make Extruder" -> "Parameterize Extruder" -> "Add Extruder to Cut List" -> "Make Extruder CAM";
            label = "Developer 2";
            color="#3a7ca8"
        }

        "Initialize Workbench" -> "Make Axis";
        "Initialize Workbench" -> "Make Extruder";
    }

.. Important:: Each step in the above process may not apply to all parts depending upon requirements.

1. Initialize Workbench
-----------------------
1. Use the ``osewb init`` command to initialize a new workbench.
2. Create a git repository and host it on a centralized platform like GitHub.

2. Make Parts
-------------
1. Add packages for each part in the `part package <app_package.html#part-sub-package>`_ and corresponding `part classes <part_classes.html>`_.
2. Add icons for each part in the `icon package <gui_package.html#icon-sub-package>`_.
3. Add packages for each part in the `command package <gui_package.html#command-sub-package>`_ and corresponding `command classes <command_classes.html>`_ that call the part classes.
4. Register that command in the `command registry module <gui_package.html#command-registry-module>`_ and associate it to the **main toolbar**.

3. Parameterize Parts
---------------------
1. Add packages for each part in the `model package <app_package.html#model-sub-package>`_ and corresponding `model classes <model_classes.html>`_.
2. Add packages for each part in the `part feature package <gui_package.html#part-feature-sub-package>`_ and corresponding part feature creation functions.
3. Refactor the corresponding command class to call the newly created part feature creation function instead of the part classes.

4. Attachment
-------------
1. Add packages for each attachment relationship in the `attachment package <app_package.html#attachment-sub-package>`_ and corresponding `attachment functions <attachment_functions.html>`_.
2. Refactor the corresponding command class to call the attachment function, and refactor part feature creation function, model, and part classes as needed.

5. Cut List Generation
----------------------
1. Add commands for generating a cut list.
2. Modify the ``build_cut_list`` function as needed for each part.

6. CAM File Generation
-----------------------
1. Modify part classes with as much detail as needed for CAM file generation. If a lot of detail is needed, then refactor the part class to support making a simplified or detailed version.
2. If needed, created a new command for exposing the detailed version of the part and expose that to the user through the **main menu** while the **main toolbar** exposes the simplified version for modeling purposes.
