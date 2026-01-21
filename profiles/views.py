import logging
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    Display a list of all profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered profiles index page.
    """
    try:
        profiles_list = Profile.objects.all()
    except Exception as e:
        profiles_list = []
        logger.error(f"Database error when fetching profiles: {e}")
    context = {'profiles_list': profiles_list}

    return render(request, 'profiles/index.html', context)


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Display a specific user profile.

    Args:
        request (HttpRequest): The HTTP request sent by the user.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The rendered HTML response for the profile detail page.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning(f"Profile with username {username} does not exist")
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error(f"Database error fetching profile {username}: {e}")
        return render(request, '500.html', status=500)
    context = {'profile': profile}

    return render(request, 'profiles/profile.html', context)
