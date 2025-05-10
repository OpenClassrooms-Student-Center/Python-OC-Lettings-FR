import logging
from django.shortcuts import render
from django.http import Http404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of profiles.

    Retrieves all Profile objects and renders the 'profiles/index.html' template.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered page with the list of profiles.
    :rtype: HttpResponse
    """
    try:
        logger.info('Accessing profiles index page')
        profiles_list = Profile.objects.all()
        logger.debug(f'Found {len(profiles_list)} profiles')
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f'Error retrieving profiles list: {str(e)}', exc_info=True)
        raise


def profile(request, username):
    """
    Display the details of a specific user profile.

    Retrieves the Profile object corresponding to the provided username and
    renders the 'profiles/profile.html' template with its details.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param username: The username of the profile to display.
    :type username: str
    :return: The rendered page with the profile details.
    :rtype: HttpResponse
    :raises Http404: If no profile matches the provided username.
    """
    try:
        logger.info(f'Accessing profile detail page for username: {username}')
        profile = Profile.objects.get(user__username=username)
        logger.debug(f'Retrieved profile for user: {username}')
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.warning(f'Profile not found with username: {username}')
        raise Http404("Profile does not exist")
    except Exception as e:
        logger.error(
            f'Error retrieving profile for username {username}: {str(e)}',
            exc_info=True
        )
        raise
