"""URL configuration for the profiles application.

This module defines the URL patterns that route incoming HTTP
requests to the profiles views.
"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/", views.edit_profile, name="edit"),
    path("<str:username>/", views.profile, name="profile"),
]
