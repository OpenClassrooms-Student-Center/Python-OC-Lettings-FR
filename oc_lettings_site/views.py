from django.shortcuts import render


def index(request):
    """Render the index page.

    This view renders the index.html template, typically serving as the homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response containing the index page.
    """
    return render(request, 'index.html')
