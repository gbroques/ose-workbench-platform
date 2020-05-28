.. {{ cookiecutter.workbench_title }} documentation master file, created by
   sphinx-quickstart on Wed Feb 19 00:49:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


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
