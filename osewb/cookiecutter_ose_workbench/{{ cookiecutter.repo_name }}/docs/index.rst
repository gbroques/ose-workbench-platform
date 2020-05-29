{{ cookiecutter.workbench_title }} Documentation
{% for character in range(cookiecutter.workbench_title|length) -%}={% endfor %}==============

A FreeCAD workbench for designing {{ cookiecutter.machine_display_name }} machines by `Open Source Ecology <https://www.opensourceecology.org/>`_ (OSE).

.. toctree::
   :maxdepth: 2
   :caption: {{ cookiecutter.machine_title }} Package

   {{ cookiecutter.base_package }}/{{ cookiecutter.base_package }}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
