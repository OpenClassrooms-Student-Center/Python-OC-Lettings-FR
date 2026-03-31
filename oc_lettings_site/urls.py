"""Root URL configuration for the oc_lettings_site project.

This module routes incoming HTTP requests to the appropriate
application URLs and defines custom error handlers.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpRequest, HttpResponse

from . import views


def trigger_error(request: HttpRequest) -> HttpResponse:
    """Intentionally raise an error to test Sentry integration.

    This view is used to trigger a 500 error and verify that
    Sentry correctly captures and reports the exception.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: This function never returns normally, it always raises.
    """
    raise ZeroDivisionError("Test Sentry - division par zéro")


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
    path("accounts/", include("accounts.urls")),
    path("contact/", include("contact.urls")),
]

# Custom error handlers
handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"
