"""
Views module for lettings app
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Letting
from monitoring import logger


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis in
# faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request: HttpRequest) -> HttpResponse:
    """
    View function for lettings index page
    Args:
        request (HttpRequest): Http Request object

    Returns:
        An HTTP response with the list of lettings or an HTTP response with 500 error.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}

        logger.info(f"Going to lettings index page : {context=}, status = 200.")

        return render(request, template_name='lettings/index.html', context=context, status=200)

    except Exception as e:
        context = {"error": str(e)}

        logger.error(f"Error 500 returned while reaching lettings index page : {context=},"
                     f" status = 500.")

        return render(request, template_name='error_500.html', context=context, status=500)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut
# luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan interdum. Ut quis urna
# pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum,
# tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor
# risus. Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt
# enim, ac lacinia augue pulvinar sit amet.
def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    View function for letting detail page
    Args:
        request (HttpRequest): Http Request object
        letting_id (int): letting id

    Returns:
        An HTTP response with the letting detail or an HTTP response with 404 error if not found
        or an HTTP response with 500 error
    """
    try:
        letting = Letting.objects.get(id=letting_id)

        context = {
            'title': letting.title,
            'address': letting.address,
        }

        logger.info(f"Going to lettings details page : {context=}, status = 200.")

        return render(request, template_name='lettings/letting.html', context=context, status=200)

    except Letting.DoesNotExist as e:
        context = {"type": "letting", "id": letting_id, "error": str(e)}

        logger.warning(f"Error 404 returned while reaching letting n°{letting_id} : {context=},"
                       f" status = 404.")

        return render(request, template_name='error_404.html', context=context, status=404)

    except Exception as e:
        context = {"error": str(e)}

        logger.error(f"Error 500 returned while reaching letting details page : {context=},"
                     f" status = 500.")

        return render(request, template_name='error_500.html', context=context, status=500)
