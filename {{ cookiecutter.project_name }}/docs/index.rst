{% set title = cookiecutter.project_name + " docs" -%}
{{ title }}
{{ title|length * "=" }}

.. toctree::
   :maxdepth: 2
   :name: mastertoc

   {{ cookiecutter.project_slug }}

This documentation was last updated on |today|
