from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


from . import views


def custom_404(request, exception):
    """
    Custom 404 error handler.

    This function renders a custom 404 error page when a page is not found.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that was raised.

    Returns:
        HttpResponse: The rendered HTML of the custom 404 error page with a 404 status.
    """
    return render(request, '404.html', status=404)


# Assign the custom 404 handler
handler404 = custom_404

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls'), name='lettings'),
    path('profiles/', include('profiles.urls'), name='profiles'),
    path('admin/', admin.site.urls),
]
"""
URL configuration for the project.

This module defines the URL patterns for the project, including the admin interface,
index page, and includes for the 'lettings' and 'profiles' apps. It also sets a custom
404 error handler.

Routes:
    - '' (root): Directs to the index view.
    - 'lettings/': Includes the URL patterns from the 'lettings' app.
    - 'profiles/': Includes the URL patterns from the 'profiles' app.
    - 'admin/': Directs to the admin interface.

Attributes:
    handler404 (function): The custom 404 error handler function.
"""
