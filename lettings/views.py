from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    Display a list of all lettings.

    Args:
        request (HttpRequest): The HTTP request sent by the user.

    Returns:
        HttpResponse: The rendered lettings index page.
    """
    try:
        lettings_list = Letting.objects.all()
    except Exception as e:
        lettings_list = []
        logger.error(f"Database error when fetching lettings: {e}")

    context = {'lettings_list': lettings_list}

    return render(request, 'lettings/index.html', context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Display a specific letting.

    Args:
        request (HttpRequest): The HTTP request sent by the user.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered HTML response for the letting detail page.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning(f"Letting with id {letting_id} does not exist")
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error(f"Database error fetching letting {letting_id}: {e}")
        return render(request, '500.html', status=500)

    context = {
        'title': letting.title,
        'address': letting.address,
    }

    return render(request, 'lettings/letting.html', context)
