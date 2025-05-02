"""Views for lettings app."""

import logging
from django.shortcuts import render
from django.http import Http404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Display the list of all lettings.

    Retrieves all Letting objects from the database and renders them in the index template.

    :param request: The HTTP request object
    :type request: django.http.HttpRequest
    :return: Rendered template with the list of lettings
    :rtype: django.http.HttpResponse
    :raises Exception: If there is an error retrieving the lettings list
    """
    try:
        logger.info('Accessing lettings index page')
        lettings_list = Letting.objects.all()
        logger.debug(f'Found {len(lettings_list)} lettings')
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f'Error retrieving lettings list: {str(e)}', exc_info=True)
        raise


def letting(request, letting_id):
    """
    Display details for a specific letting.

    Retrieves a Letting object by its ID and renders the letting detail template.

    :param request: The HTTP request object
    :type request: django.http.HttpRequest
    :param letting_id: The ID of the letting to display
    :type letting_id: int
    :return: Rendered template with letting details
    :rtype: django.http.HttpResponse
    :raises Http404: If no letting matches the provided ID
    :raises Exception: For any other errors
    """
    try:
        logger.info(f'Accessing letting detail page for ID: {letting_id}')
        letting = Letting.objects.get(id=letting_id)
        logger.debug(f'Retrieved letting: {letting.title}')
        context = {
            'title': letting.title,
            'letting': letting,
            'address': letting.address
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.warning(f'Attempted to access non-existent letting with ID: {letting_id}')
        raise Http404("Letting does not exist")
    except Exception as e:
        logger.error(
            f'Error retrieving letting details for ID {letting_id}: {str(e)}',
            exc_info=True
            )
        raise
