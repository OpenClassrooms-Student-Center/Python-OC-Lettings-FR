"""
Views for the ``lettings`` application.

This module provides the views responsible for displaying the list
of available lettings and the details of a specific letting.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Letting

import logging

logger = logging.getLogger(__name__)


def lettings_index(request: HttpRequest) -> HttpResponse:
    """
    Render the page listing all available lettings.

    This view retrieves all lettings from the database and displays them
    on the lettings index page.

    An informational log entry is generated whenever the page is accessed.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :returns: Rendered lettings index page.
    :rtype: HttpResponse
    """
    logger.info(
        "Lettings list accessed",
        extra={
            "path": request.path,
            "method": request.method,
        },
    )
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Render the page displaying details of a specific letting.

    This view retrieves a letting by its unique identifier and displays
    its details on the letting detail page.

    An informational log entry is generated whenever the page is accessed.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :param letting_id: Unique identifier of the letting.
    :type letting_id: int
    :returns: Rendered letting detail page.
    :rtype: HttpResponse
    """
    logger.info(
        "Letting detail accessed",
        extra={
            "letting_id": letting_id,
            "path": request.path,
            "method": request.method,
        },
    )
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
