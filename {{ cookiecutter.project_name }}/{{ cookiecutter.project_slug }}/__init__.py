"""{{ cookiecutter.project_description }}."""
{%- if cookiecutter.include_entry_point == "y" %}
from ._main import main
from ._version import __version__

__all__ = ["__version__", "main"]
{%- else %}
from ._version import __version__

__all__ = ["__version__"]
{%- endif %}
