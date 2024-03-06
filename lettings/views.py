from django.shortcuts import render
from .models import Letting
from oc_lettings_site.utils import send_to_sentry_message
from oc_lettings_site.logger import capture_sentry_message


def index(request):
    """
    Display an index with a list of :model:`lettings.letting`.

    **Context**

    ``lettings_list``
        A list of instances of :model:`lettings.letting`.

    **Template:**

    :template:`lettings/index.html`

    """
    send_to_sentry_message("lettings", request.user,
                           "Consultation de la liste des lettings")
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# capture Exception and send to capture_sentry_message
@capture_sentry_message
def letting(request, letting_id):
    """
    Display an individual letting of :model:`lettings.letting`.

    **Context**

    ``letting``
        An instance of :model:`lettings.letting` containing a title and
        an address.

    **Template:**

    :template:`letting.html`

    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
