"""
{% set title = cookiecutter.project_slug + ".__main__" -%}
{{ title }}
{{ title|length * "=" }}

Module entry point.
"""
from {{ cookiecutter.project_slug }} import main

if __name__ == "__main__":
    main()
