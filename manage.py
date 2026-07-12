"""
Management script for the Django project.

This module serves as the command-line utility for administrative tasks
in the Django project, such as running the development server,
applying migrations, creating superusers, and executing custom management commands.

It sets the default settings module for the Django project and
delegates execution to Django's built-in command-line utility.
"""

import os
import sys


def main():
    """
    Entrypoint for the Django management script.

    Ensures that the DJANGO_SETTINGS_MODULE environment variable is set
    to the project's settings module and invokes Django's
    execute_from_command_line function to handle command-line arguments.

    Raises:
        ImportError: If Django is not installed or cannot be imported.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
