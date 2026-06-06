"""
Views module for profiles app
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from monitoring import logger

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

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}

    logger.info(f"Going to profiles index page : {context=}, status = 200.")

    return render(request=request,
                  template_name='profiles/index.html',
                  context=context,
                  status=200)


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

    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}

    logger.info(f"Going to profile details page : {context=}, status = 200.")

    return render(request, template_name='profiles/profile.html', context=context, status=200)
