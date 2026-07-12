"""
URL configuration for the ``profiles`` application.

This module maps the application's URL patterns to the corresponding
view functions and defines the namespace used for URL resolution.
"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    # Root path: displays the list of all available profiles
    path("", views.profiles_index, name="profiles_index"),

    # Dynamic route: displays details for a specific profile
    # identified by the username
    path("<str:username>/", views.profile, name="profile"),
]
