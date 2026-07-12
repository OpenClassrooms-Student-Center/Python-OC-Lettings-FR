"""
Root URL configuration for the Orange County Lettings project.

This module defines the application's main URL routing, including the
home page, the Django administration interface and the URL configurations
of the ``lettings`` and ``profiles`` applications.

Custom handlers for HTTP 404 and 500 errors are also registered here.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Lettings app: routes are defined in lettings.urls
    path("lettings/", include("lettings.urls")),
    # Profiles app: routes are defined in profiles.urls
    path("profiles/", include("profiles.urls")),
    # Django admin interface
    path("admin/", admin.site.urls),
]


# Error handling:

handler404 = "oc_lettings_site.views.page_not_found"
handler500 = "oc_lettings_site.views.server_error"
