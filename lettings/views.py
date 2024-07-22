import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError
from lettings.models import Letting

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the index page of lettings.

    This view retrieves all lettings from the database and passes them to the template for
    rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML of the index page.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        logger.debug("Index view accessed, retrieved lettings list.")
        return render(request, "lettings/index.html", context)
    except Exception as e:
        logger.error(f"Error in index view: {e}")
        return HttpResponseServerError("Internal server error")


def letting(request, letting_id):
    """
    View function for an individual letting page.

    This view retrieves a specific letting based on the provided letting_id and passes its details
    to the template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: The rendered HTML of the letting detail page.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        logger.debug(f"Letting view accessed, retrieved letting with id {letting_id}.")
        return render(request, "lettings/letting.html", context)
    except Letting.DoesNotExist:
        logger.warning(f"Letting with id {letting_id} does not exist.")
        return render(request, "404.html", status=404)
    except Exception as e:
        logger.error(f"Error in letting view: {e}")
        return HttpResponseServerError("Internal server error")
