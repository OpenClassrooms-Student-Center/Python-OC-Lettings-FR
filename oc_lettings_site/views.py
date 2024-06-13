from django.shortcuts import render
from sentry_sdk import capture_exception, capture_message


def index(request):
    """
    Render the index.html template.
    """
    return render(request, 'oc_lettings_site/index.html')


def handle_404(request, exception):
    """
    Render the 404.html template.
    """
    capture_message('Page not found (404)', level='info')
    return render(request, 'oc_lettings_site/404.html', status=404)


def handle_500(request):
    """
    Render the 500.html template.
    """
    capture_message('Internal server error (500)', level='error')
    return render(request, 'oc_lettings_site/500.html', status=500)


def get_500(request):
    # Ligne ajoutée pour provoquer une erreur 500
    try:
        raise Exception("Ceci est une erreur 500 test.")
    except Exception as e:
        capture_exception(e)
        raise e
