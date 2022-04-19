"""
{% set title = cookiecutter.project_slug + "._main" -%}
{{ title }}
{{ title|length * "=" }}

Contains package entry point.
"""


def main() -> int:
    """Main function for package.

    :return: Exit status.
    """
    return 0
