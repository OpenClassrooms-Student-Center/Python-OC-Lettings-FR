"""Views for the main OC Lettings site.

This module provides the home page view and custom handlers
for 404 and 500 HTTP error responses.
"""

from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """Display the home page.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: The rendered home page.
    """
    latest_lettings = Letting.objects.select_related("address").order_by("-id")[:3]
    context = {
        "latest_lettings": latest_lettings,
        "lettings_count": Letting.objects.count(),
    }
    return render(request, "index.html", context)


def custom_404(request, exception):
    """Render the custom 404 error page.

    Args:
        request: HttpRequest object representing the current request.
        exception: The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page with a 404 status.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """Render the custom 500 error page.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: The rendered 500 error page with a 500 status.
    """
    return render(request, "500.html", status=500)
