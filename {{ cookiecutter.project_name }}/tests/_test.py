"""
tests._test
===========
"""
import pytest

import {{ cookiecutter.project_slug }}


def test_version(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test ``{{ cookiecutter.project_slug }}.__version__``.

    :param monkeypatch: Mock patch environment and attributes.
    """
    version = "0.1.0"
    monkeypatch.setattr("{{ cookiecutter.project_slug }}.__version__", version)
    assert {{ cookiecutter.project_slug }}.__version__ == version
{%- if cookiecutter.include_entry_point == "y" %}


def test_main(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
) -> None:
    """Test ``{{ cookiecutter.project_slug }}.main``.

    :param monkeypatch: Mock patch environment and attributes.
    :param capsys: Capture and return stdout and stderr stream.
    """
    message = "Hello, world!"
    monkeypatch.setattr("{{ cookiecutter.project_slug }}.main", lambda: print(message))
    {{ cookiecutter.project_slug }}.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == message


def test_exit_status() -> None:
    """Test ``{{ cookiecutter.project_slug }}.main`` exit status."""
    assert {{ cookiecutter.project_slug }}.main() == 0
{%- endif %}
