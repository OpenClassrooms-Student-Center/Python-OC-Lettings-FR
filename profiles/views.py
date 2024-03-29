from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """Render the index page with a list of all profiles.

    This view retrieves all profiles from the database and passes
    them to the 'profiles/index.html' template to render the index page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response containing the index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Render the profile page for a specific user.

    This view retrieves the profile associated with the given username
    from the database and passes it to the 'profiles/profile.html' template
    to render the profile page.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being viewed.

    Returns:
        HttpResponse: The rendered HTML response containing the profile page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
