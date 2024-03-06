from django.shortcuts import render
from .models import Profile
from oc_lettings_site.utils import send_to_sentry_message
from oc_lettings_site.logger import capture_sentry_message


def profiles_index(request):
    """
    Display an index with a list of :model:`profiles.profile`.

    **Context**

    ``profiles_list``
        A list of instances of :model:`profiles.profile`.

    **Template:**

    :template:`profiles_index.html`

    """
    send_to_sentry_message("profiles", request.user,
                           "Consultation de la liste des profiles")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# capture Exception and send to capture_sentry_message
@capture_sentry_message
def profile(request, username):
    """
    Display an individual profile of :model:`profiles.profile`.

    **Context**

    ``profile``
        An instance of :model:`profiles.profile`.

    **Template:**

    :template:`letting.html`

    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
