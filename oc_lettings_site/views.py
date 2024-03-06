from django.shortcuts import render
from oc_lettings_site.utils import send_to_sentry_exception


def index(request):
    """
    Display an index with two clickable buttons lettings and profiles.

    **Template:**

    :template:`index.html`

    """
    return render(request, 'index.html')


# custom 404 view
def custom_404(request, exception):
    """
    Display an error page 404 when a user attempts to follow a broken or
    dead link.

    **Template:**

    :template:`404.html`

    """
    send_to_sentry_exception("Page Not Found",
                             f"{request.path_info}{request.META}", exception)

    return render(request, '404.html', status=404)


# custom 500 view
def custom_500(request):
    """
    Display an error page 500 when a the server encountered an unexpected
    condition that prevented it from fulfilling the request.

    **Template:**

    :template:`500.html`

    """
    return render(request, '500.html', status=500)
