"""
View functions for the 'profiles' application, handling the listing and detail pages for user profiles.
"""
import logging

from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger('oc_lettings_site')


def index(request):
    """
    Renders the index page for all user profiles.

    Retrieves all Profile objects from the database and passes them to the template.

    Args:
        request (HttpRequest): The HTTP request object.

    Context:
        profiles_list (QuerySet): A list of all available Profile objects.
    """
    # Log entry into the function
    logger.info("Accessing profiles index view.")

    try:
        # Database operation wrapped in try/except for error monitoring
        profiles_list = Profile.objects.all()
        # Log success with details (using debug level for routine success)
        logger.debug(f"Successfully retrieved {len(profiles_list)} profiles.")
    except Exception as e:
        # Log a critical error if database access fails. This will be sent to Sentry.
        logger.error(f"Critical error retrieving profiles list from DB: {e}", exc_info=True)
        # Re-raise the exception to trigger the Django 500 error handler and Sentry capture
        raise 

    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Renders the detail page for a specific user profile.

    Retrieves a single Profile object based on the username. Returns a 404 error if not found.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username associated with the Profile to retrieve.

    Context:
        profile (Profile): The retrieved Profile object.
    """
    # Log entry into the function with the primary key
    logger.info(f"Accessing detail view for profile username: {username}")

    try:
        # Use get_object_or_404 to handle the DoesNotExist scenario gracefully
        profile = get_object_or_404(Profile, user__username=username)
        logger.debug(f"Retrieved profile for user: {username}")
    except Profile.DoesNotExist:
        # Log a warning when a requested object is not found (this becomes a 404, not a 500)
        logger.warning(f"Profile for user '{username}' does not exist in the database.")
        raise # Re-raise the exception for Django to process the 404
    except Exception as e:
        # Catch other potential database errors (e.g., connection issue)
        logger.error(f"Unexpected error accessing profile for user '{username}': {e}", exc_info=True)
        raise

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)