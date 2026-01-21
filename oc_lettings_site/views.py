from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the home page of the Holiday Homes website.

    Args:
        request (HttpRequest): The HTTP request sent by the user.

    Returns:
        HttpResponse: The rendered HTML response of the home page.
    """

    return render(request, 'index.html')


def custom_404(request: HttpRequest, exception) -> HttpResponse:
    """
    Custom 404 error handler.

    Args:
        request (HttpRequest): The HTTP request sent by the user.
        exception: The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered HTML response for the 404 error page.
    """
    return render(request, '404.html', status=404)


def custom_500(request: HttpRequest) -> HttpResponse:
    """
    Custom 500 error handler.

    Args:
        request (HttpRequest): The HTTP request sent by the user.

    Returns:
        HttpResponse: The rendered HTML response for the 500 error page.
    """
    return render(request, '500.html', status=500)
