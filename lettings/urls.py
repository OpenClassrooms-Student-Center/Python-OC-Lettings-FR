from django.urls import path
from . import views

"""URL configuration for the 'lettings' app.

This module defines URL patterns for the 'lettings' app, mapping
URL patterns to view functions.

Attributes:
    app_name (str): The namespace for the URLs in this module.
        This allows you to refer to these URLs using their namespaced
        names like 'lettings:index' or 'lettings:letting'.
    urlpatterns (list): A list of `path` objects that define the
        URL patterns for the 'lettings' app.
"""

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
