"""
Root view functions for the main project site, including the homepage 
and custom handlers for 404 and 500 errors.
"""
from django.shortcuts import render
import sentry_sdk

def index(request):
    """
    Renders the main index (homepage) of the application.

    Args:
        request (HttpRequest): The HTTP request object.
    """
    return render(request, 'index.html')


def custom_404_view(request, exception):
    """
    Renders the custom 404 (Page Not Found) error page.

    This function is used by the Django handler404. It ensures the response 
    returns an HTTP 404 status code.

    Args:
        request (HttpRequest): The HTTP request object.
        exception: The exception object passed by Django (required signature).
    """
    return render(request, '404.html', status=404)


def custom_500_view(request):
    """
    Renders the custom 500 (Internal Server Error) page.

    This function is used by the Django handler500. It ensures the response 
    returns an HTTP 500 status code.

    Args:
        request (HttpRequest): The HTTP request object.
    """
    return render(request, '500.html', status=500)


# oc_lettings_site/views.py (For testing purposes only)
# def index(request):
#     # Intentional error to force a 500 status
#     raise Exception("Intentional Server Crash for 500 Test") 
#     return render(request, 'index.html')


# def index(request):
#     """
#     Renders the main index (homepage) of the application.
#     """
#     sentry_sdk.capture_message("SENTRY_DIRECT_TEST: This message should always appear as a new Issue.", 'fatal')
    
#     return render(request, 'index.html')