"""WSGI config for the oc_lettings_site project.

This module exposes the WSGI callable as a module-level variable named
``application``. It is used by WSGI servers to forward HTTP requests
to the Django application.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

application = get_wsgi_application()
