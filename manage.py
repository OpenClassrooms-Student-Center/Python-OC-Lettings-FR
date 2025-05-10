"""
Django's command-line utility for administrative tasks.

This module contains the main entry point for executing Django administrative commands.
It handles setting up the Django environment and running management commands.
"""

import os
import sys


def main():
    """
    Sets up the Django environment by configuring the default settings module
    and executes the requested management command.


    :raises ImportError: If Django cannot be imported, likely due to not being installed
        or the virtual environment not being activated.
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
