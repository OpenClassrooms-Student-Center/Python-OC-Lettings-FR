"""
Views for the main Django project (oc_lettings_site).

This module defines the views responsible for rendering the application's
home page and custom HTTP error pages.
"""

from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the application's home page.

    This view handles requests to the root URL (``/``) and returns
    the main landing page of the Orange County Lettings application.

    An informational log entry is generated each time the page is
    successfully accessed.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :returns: Rendered home page.
    :rtype: HttpResponse
    """
    logger.info("Homepage accessed")

    return render(request, "index.html")


def page_not_found(request, exception):
    """
    Render the custom 404 error page.

    This view is invoked when Django cannot resolve the requested URL.

    A warning is logged to record the requested path and HTTP method.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :param exception: URL resolution exception.
    :type exception: Exception
    :returns: Rendered 404 error page.
    :rtype: HttpResponse
    """
    logger.warning("404 error encountered", extra={"path": request.path, "method": request.method})
    return render(request, "404.html", status=404)


def server_error(request):
    """
    Render the custom 500 error page.

    This view is called whenever an unhandled server error occurs.

    An error is logged to facilitate monitoring and post-mortem debugging.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :returns: Rendered 500 error page.
    :rtype: HttpResponse
    """
    logger.error("500 error encountered", extra={"path": request.path, "method": request.method})
    return render(request, "500.html", status=500)
