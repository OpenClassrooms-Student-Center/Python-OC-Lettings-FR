import logging
from django.shortcuts import render
from django.http import HttpResponseServerError

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the index page.

    This view renders the main index page of the website.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML of the index page.
    """
    try:
        logger.debug("Index view accessed.")
        return render(request, "index.html")
    except Exception as e:
        logger.error(f"Error in index view: {e}")
        return HttpResponseServerError("Internal server error")
