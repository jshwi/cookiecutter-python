"""
{% set title = cookiecutter.project_slug + "._main" -%}
{{ title }}
{{ title|length * "=" }}

Contains package entry point.
"""


def main() -> None:
    """Main function for package."""
