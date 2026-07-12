"""
ASGI configuration for the oc_lettings_site project.

This module exposes the ASGI callable as a module-level variable
named ``application``.

It is used by ASGI-compatible web servers to serve the Django
application and enables support for asynchronous features
such as WebSockets or long-lived connections.
"""

import os

from django.core.asgi import get_asgi_application

# Set the default Django settings module for the ASGI application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# ASGI application callable used by compatible servers
application = get_asgi_application()
