"""
post_gen_project
================

This script is invoked after a project is generated.
"""
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
GITHUB_USERNAME = "{{ cookiecutter.github_username }}"
ORIGIN = f"git@github.com:{GITHUB_USERNAME}/{PROJECT_NAME}"


if "{{ cookiecutter.include_entry_point }}" == "n":
    os.remove(os.path.join(PROJECT_DIRECTORY, PROJECT_SLUG, "_main.py"))
    os.remove(os.path.join(PROJECT_DIRECTORY, PROJECT_SLUG, "__main__.py"))
    os.remove(os.path.join(PROJECT_DIRECTORY, ".pre-commit-hooks.yaml"))

subprocess.run(["poetry", "install"], check=True)
subprocess.run(["npm", "install"], check=True)
subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
subprocess.run(["git", "remote", "add", "origin", ORIGIN], check=True)
subprocess.run(["git", "checkout", "-b", "dev/main"], check=True)
subprocess.run(["npm", "run", "audit"], check=True)
