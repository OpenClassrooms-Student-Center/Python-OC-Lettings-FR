from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the main index page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered index page.
    :rtype: HttpResponse
    """
    try:
        logger.info('Accessing main index page')
        return render(request, 'index.html')
    except Exception as e:
        logger.error(f'Error rendering index page: {str(e)}', exc_info=True)
        raise


def error_404(request, exception):
    """
    Render the 404 error page when a page is not found.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param exception: The exception raised when the requested page is not found.
    :type exception: Exception
    :return: The rendered 404 error page.
    :rtype: HttpResponse
    """
    logger.warning(f"404 error: Page not found - {request.path}", exc_info=True)
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Render the 500 error page when a server error occurs.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered 500 error page.
    :rtype: HttpResponse
    """
    logger.error("500 error: Server error occurred", exc_info=True)
    return render(request, '500.html', status=500)
