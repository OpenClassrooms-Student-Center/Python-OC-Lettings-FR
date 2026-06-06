"""
Views module for oc_lettings_site app
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from monitoring import init_sentry, logger


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae erat
# ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request: HttpRequest) -> HttpResponse:
    """
    View function for home page
    Args:
        request (HttpRequest): Http Request object

    Returns:
        An HTTP response with index page or HTTP response with 500 error.
    """
    init_sentry()

    logger.info(f"Going to home page : status = 200.")

    return render(request=request, template_name='oc_lettings_site/index.html')


def custom_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    """
    Custom 404 view function
    Args:
        request (Request): Http Request object
        exception (Exception): Exception object

    Returns:
        An HTTP response with 404 page
    """
    path = request.path
    elements = path.split("/")

    context_type = elements[1][:-1]
    element = str(elements[-2])

    context = {"type": context_type,
               "element": element,
               "error": str(exception)}

    return render(request=request,
                  template_name="oc_lettings_site/404.html",
                  context=context,
                  status=404)


def custom_500(request: HttpRequest) -> HttpResponse:
    """
    Custom 500 view function
    Args:
        request (Request): Http Request object

    Returns:
        An HTTP response with 500 page
    """
    return render(request=request,
                  template_name="oc_lettings_site/500.html",
                  status=500)
