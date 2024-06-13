from django.shortcuts import render, get_object_or_404
from .models import Letting
from sentry_sdk import capture_exception, capture_message


def lettings_index(request):
    """
    Get all lettings from the database and
    render the lettings_index.html template.
    """
    try:
        lettings_list = Letting.objects.all()
        capture_message('Lettings index accessed', level='info')
    except Exception as e:
        capture_exception(e)
        raise e
    context = {'lettings_list': lettings_list}

    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Get a letting by its id and render
    the letting.html template with context.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        capture_message(f'Letting accessed: {letting_id}', level='info')
        context = {
            'title': letting.title,
            'address': letting.address,
        }
    except Exception as e:
        capture_exception(e)
        raise e
    return render(request, 'lettings/letting.html', context)
