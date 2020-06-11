{{ cookiecutter.workbench_title }} Documentation
{% for character in range(cookiecutter.workbench_title|length) -%}={% endfor %}==============

A FreeCAD workbench for designing {{ cookiecutter.machine_display_name }} machines by `Open Source Ecology (OSE) <https://www.opensourceecology.org/>`_.

For more information on codebase conventions and patterns, see the `OSE Workbench Platform <https://ose-workbench-platform.readthedocs.io/en/latest/>`_.

.. toctree::
   :maxdepth: 2
   :caption: Library Package

   {{ cookiecutter.base_package }}/{{ cookiecutter.base_package }}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
