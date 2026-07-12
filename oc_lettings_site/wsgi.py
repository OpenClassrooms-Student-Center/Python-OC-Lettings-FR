"""
WSGI config for oc_lettings_site project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It exposes the WSGI callable as a module-level
variable named `application`.

WSGI (Web Server Gateway Interface) is a specification that describes how a web server
communicates with web applications.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'oc_lettings_site' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

# WSGI application callable for serving the project.
application = get_wsgi_application()
