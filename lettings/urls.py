"""
URL configuration for the ``lettings`` application.

This module maps URL patterns to their corresponding view functions
and defines the namespace used for URL resolution.
"""

from django.urls import path

from . import views

app_name = "lettings"
urlpatterns = [
    # Root path: displays the list of all available lettings
    path("", views.lettings_index, name="lettings_index"),

    # Dynamic route: displays details for a specific letting
    # identified by its primary key (letting_id)
    path("<int:letting_id>/", views.letting, name="letting"),
]
