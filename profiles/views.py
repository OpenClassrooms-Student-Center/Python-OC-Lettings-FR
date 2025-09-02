from django.shortcuts import render, get_object_or_404
from .models import Profile

def index(request):
    """
    View function for the profiles list page.
    
    Args:
        request: The HTTP request object
        
    Returns:
        Rendered template 'profiles/index.html' with a list of all profiles
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

def profile(request, username):
    """
    View function for displaying a specific user's profile.
    
    Args:
        request: The HTTP request object
        username: The username of the profile to display
        
    Returns:
        Rendered template 'profiles/profile.html' with the requested profile
        
    Raises:
        Http404: If the profile with the given username doesn't exist
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
