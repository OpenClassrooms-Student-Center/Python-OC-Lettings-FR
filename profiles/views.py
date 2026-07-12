"""
Views for the ``profiles`` application.

This module provides the views responsible for displaying the list
of user profiles and individual profile details.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile

import logging

logger = logging.getLogger(__name__)


def profiles_index(request):
    """
    Render the page listing all user profiles.

    This view handles requests to the profiles index page and displays
    every available profile.

    An informational log entry is generated whenever the page is accessed.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :returns: Rendered profiles index page.
    :rtype: HttpResponse
    """

    logger.info(
        "Profiles list accessed",
        extra={
            "path": request.path,
            "method": request.method,
        },
    )
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Render the detail page of a user profile.

    This view retrieves the profile associated with the provided username
    and displays its information.

    An informational log entry is generated whenever a profile is viewed.

    :param request: Incoming HTTP request.
    :type request: HttpRequest
    :param username: Username identifying the requested profile.
    :type username: str
    :returns: Rendered profile detail page.
    :rtype: HttpResponse
    :raises Http404: If no matching profile exists.
    """

    logger.info(
        "Profile detail accessed",
        extra={
            "username": username,
            "path": request.path,
            "method": request.method,
        },
    )
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
