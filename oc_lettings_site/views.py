"""
Views module for oc_lettings_site app
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


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
    try:
        return render(request, template_name='index.html')

    except Exception as e:
        context = {'error': str(e)}
        return render(request, template_name='error_500.html', context=context)
