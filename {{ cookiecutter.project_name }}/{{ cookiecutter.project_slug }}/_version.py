"""
{% set title = cookiecutter.project_slug + "._version" -%}
{{ title }}
{{ title|length * "=" }}

Contains the version of this package.

Allows for access to the version internally without cyclic imports
caused by accessing it through __init__.
"""
__version__ = "{{ cookiecutter.project_version }}"
