from django.contrib import admin
from django.urls import path, include

from . import views

"""URL configuration for the Django project.

This module defines the URL patterns for the Django project.
It includes patterns for the index page, admin site, lettings app,
and profiles app.

Patterns:
    - '' : Maps to the index view, which typically serves the homepage.
    - 'admin/' : Maps to the Django admin site.
    - 'lettings/' : Includes URL patterns from the 'lettings' app,
        using the 'lettings' namespace.
    - 'profiles/' : Includes URL patterns from the 'profiles' app,
        using the 'profiles' namespace.
"""


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('sentry-debug/', trigger_error),
]
