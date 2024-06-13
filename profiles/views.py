from django.shortcuts import render, get_object_or_404
from .models import Profile
from sentry_sdk import capture_exception, capture_message


def profiles_index(request):
    """
    Get all profile objects and call the index.html
    template with the profiles_list context.
    """
    try:
        profiles_list = Profile.objects.all()
        capture_message('Profiles index accessed', level='info')
    except Exception as e:
        capture_exception(e)
        raise e
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Get a profile by its username and render
    the profile.html template with the profile context.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        capture_message(f'Profile accessed: {username}', level='info')
        context = {'profile': profile}
    except Exception as e:
        capture_exception(e)
        raise e
    return render(request, 'profiles/profile.html', context)
