{% set title = cookiecutter.project_name + " docs" -%}
{{ title }}
{{ title|length * "=" }}

|

The source code is available `here <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}>`_

|

.. toctree::
   :maxdepth: 1
   :name: mastertoc

   {{ cookiecutter.project_slug }}
   readme

* :ref:`genindex`

This documentation was last updated on |today|
