"""
{% set title = cookiecutter.project_slug + ".__main__" -%}
{{ title }}
{{ title|length * "=" }}

Module entry point.
"""
import sys as _sys

from {{ cookiecutter.project_slug }} import main

if __name__ == "__main__":
    _sys.exit(main())
