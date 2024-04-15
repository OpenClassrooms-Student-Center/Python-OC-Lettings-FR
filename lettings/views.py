from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """Render the index page with a list of lettings.

    This view retrieves all letting objects from the database
    and renders the index.html template with the list of lettings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response containing the
            index page with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Render the letting details page.

    This view retrieves the letting object with the specified ID
    from the database and renders the letting.html template with
    the letting details.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered HTML response containing the
            letting details page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
