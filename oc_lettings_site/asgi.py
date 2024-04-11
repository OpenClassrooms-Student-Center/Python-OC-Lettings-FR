import os
from django.core.asgi import get_asgi_application

"""This code initializes the ASGI application for the Django project."""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
application = get_asgi_application()
