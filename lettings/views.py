from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
from .models import Letting

logger = logging.getLogger(__name__)

def index(request):
    """
    View function for the lettings list page.
    Args:
        request: The HTTP request object
    Returns:
        template 'lettings/index.html' with a list of all lettings
    """
    try:
        lettings_list = Letting.objects.all()
        logger.info(f"Retrieved {len(lettings_list)} lettings for index page")
        return render(request, 'lettings/index.html', context={'lettings_list': lettings_list})
    except Exception as e:
        logger.error(f"Error retrieving lettings list: {str(e)}", exc_info=True)
        raise

def letting(request, letting_id):
    """
    View function for displaying a specific letting's details.
    Args:
        request: The HTTP request object
        letting_id: The ID of the letting to display
    Returns:
        template 'lettings/letting.html' with the requested letting's details
    Raises:
        Http404: If the letting with the given ID doesn't exist
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        logger.info(f"Retrieved letting {letting_id}: {letting.title}")
        return render(request, 'lettings/letting.html', context={
            'title': letting.title,
            'address': letting.address,
        })
    except Http404:
        logger.warning(f"Letting with id {letting_id} not found")
        raise
    except Exception as e:
        logger.error(f"Error retrieving letting {letting_id}: {str(e)}", exc_info=True)
        raise
