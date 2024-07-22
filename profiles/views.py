import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError
from profiles.models import Profile

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the index page of profiles.

    This view retrieves all profiles from the database and passes them to the template
    for rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML of the index page.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        logger.debug("Index view accessed, retrieved profiles list.")
        return render(request, "profiles/index.html", context)
    except Exception as e:
        logger.error(f"Error in index view: {e}")
        return HttpResponseServerError("Internal server error")


def profile(request, username):
    """
    View function for an individual profile page.

    This view retrieves a specific profile based on the provided username and passes
    its details to the template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile to retrieve.

    Returns:
        HttpResponse: The rendered HTML of the profile detail page.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile}
        logger.debug(f"Profile view accessed, retrieved profile for user {username}.")
        return render(request, "profiles/profile.html", context)
    except Profile.DoesNotExist:
        logger.warning(f"Profile for user {username} does not exist.")
        return render(request, "404.html", status=404)
    except Exception as e:
        logger.error(f"Error in profile view: {e}")
        return HttpResponseServerError("Internal server error")
