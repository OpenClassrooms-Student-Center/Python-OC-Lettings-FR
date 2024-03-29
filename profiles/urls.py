from django.urls import path
from . import views

"""URL configuration for the 'profiles' app.

This module defines URL patterns for the 'profiles' app, mapping
URL patterns to view functions.

Attributes:
    app_name (str): The namespace for the URLs in this module.
        This allows you to refer to these URLs using their namespaced
        names like 'profiles:index' or 'profiles:profile'.
    urlpatterns (list): A list of `path` objects that define the
        URL patterns for the 'profiles' app.
"""

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
