"""
Views module for profiles app
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request: HttpRequest) -> HttpResponse:
    """
    View function for profiles index page
    Args:
        request (HttpRequest): request object

    Returns:
        An HTTP response with the list of profiles or HTTP response with 500 error.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, template_name='profiles/index.html', context=context, status=200)

    except Exception as e:
        context = {"error": str(e)}
        return render(request, template_name='error_500.html', context=context, status=500)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor
# id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue. Pellentesque
# habitant morbi tristique senectus et netus et males
def profile(request: HttpRequest, username: str):
    """
    View function for profile details page
    Args:
        request (HttpRequest): request object
        username (str): username

    Returns:
        An HTTP response with the profile or HTTP response with 404 error if not found
        or an HTTP response with 500 error
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}

        return render(request, template_name='profiles/profile.html', context=context, status=200)

    except Profile.DoesNotExist:
        context = {"type": "profile", "name": username}
        return render(request, template_name='error_404.html', context=context, status=404)

    except Exception as e:
        context = {"error": str(e)}
        return render(request, template_name='error_500.html', context=context, status=500)
