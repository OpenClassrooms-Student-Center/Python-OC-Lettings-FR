from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
from .models import Profile

logger = logging.getLogger(__name__)

def index(request):
    """
    View function for the profiles list page.
    Args:
        request: The HTTP request object
    Returns:
        Rendered template 'profiles/index.html' with a list of all profiles
    """
    try:
        profiles_list = Profile.objects.all()
        logger.info(f"Retrieved {len(profiles_list)} profiles for index page")
        return render(request, 'profiles/index.html', context={'profiles_list': profiles_list})
    except Exception as e:
        logger.error(f"Error retrieving profiles list: {str(e)}", exc_info=True)
        raise

def profile(request, username):
    """
    View function for displaying a specific user's profile.
    Args:
        request: The HTTP request object
        username: The username of the profile to display
    Returns:
        Rendered template 'profiles/profile.html' with the requested profile
    Raises:
        Http404: If the profile with the given username doesn't exist
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(f"Retrieved profile for user {username}")
        return render(request, 'profiles/profile.html', context={'profile': profile})
    except Http404:
        logger.warning(f"Profile for user {username} not found")
        raise
    except Exception as e:
        logger.error(f"Error retrieving profile for user {username}: {str(e)}", exc_info=True)
        raise
