from django.shortcuts import render
from django.http import Http404
import logging

logger = logging.getLogger(__name__)

def index(request):
    """
    View function for the home page.
    Args:
        request: The HTTP request object
    Returns:
        Rendered template 'index.html'
    """
    try:
        logger.info("Rendering home page")
        return render(request, 'index.html')
    except Exception as e:
        logger.error(f"Error rendering home page: {str(e)}", exc_info=True)
        raise

def test_404(request):
    """
    Test view that raises a 404 error.
    Args:
        request: The HTTP request object
    Raises:
        Http404: Always raises a 404 error for testing purposes
    """
    logger.warning("Test 404 error page requested")
    raise Http404("Page de test 404")


def test_500(request):
    """
    Test view that raises a 500 error by performing a division by zero.
    Args:
        request: The HTTP request object
    Returns:
        This function never returns as it raises a ZeroDivisionError
    """
    logger.error("Test 500 error page requested")
    1 / 0  # Raise ZeroDivisionError
    return render(request, 'index.html')
