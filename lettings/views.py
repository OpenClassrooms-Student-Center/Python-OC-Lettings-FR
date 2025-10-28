"""
View functions for the 'lettings' application, handling the listing and detail pages for rental properties.
"""
import logging

from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger('oc_lettings_site')


def index(request):
    """
    Renders the index page for all lettings.

    Retrieves all Letting objects from the database and passes them to the template.

    Args:
        request (HttpRequest): The HTTP request object.

    Context:
        lettings_list (QuerySet): A list of all available Letting objects.
    """
    # Log entry into the function
    logger.info("Accessing lettings index view.")

    try:
        lettings_list = Letting.objects.all()
        # Log success with details (using debug level for routine success)
        logger.debug(f"Successfully retrieved {len(lettings_list)} lettings.")
    except Exception as e:
        # Log a critical error if database access fails. This will be sent to Sentry.
        logger.error(f"Critical error retrieving lettings list from DB: {e}", exc_info=True)
        raise 

    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the detail page for a specific letting.

    Retrieves a single Letting object based on its ID. Returns a 404 error if not found.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The primary key (ID) of the Letting to retrieve.

    Context:
        title (str): The title of the letting.
        address (Address): The associated Address object for the letting.
    """
    # Log entry into the function with the primary key
    logger.info(f"Accessing detail view for letting ID: {letting_id}")

    try:
        # get_object_or_404 handles the common DoesNotExist exception, but we wrap it 
        # to log database-related warnings or other critical errors.
        letting = get_object_or_404(Letting, id=letting_id)
        logger.debug(f"Retrieved letting title: {letting.title}")
    except Letting.DoesNotExist:
        # Log a warning when a requested object is not found (this becomes a 404, not a 500)
        logger.warning(f"Letting with ID {letting_id} does not exist in the database.")
        raise # Re-raise the exception for Django to process the 404
    except Exception as e:
        # Catch other potential database errors (e.g., connection issue)
        logger.error(f"Unexpected error accessing letting with ID {letting_id}: {e}", exc_info=True)
        raise

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

