"""Views for the lettings application.

This module contains the views responsible for displaying
the list of lettings and the detail of a single letting.
"""

import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting
from lettings.forms import LettingFilterForm

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of lettings.

    Retrieves all Letting objects and renders the lettings index page.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: The rendered lettings index page.
    """
    logger.info("Affichage de la liste des lettings")
    logger.info("Affichage de la liste des locations")
    form = LettingFilterForm(request.GET or None)
    lettings_list = Letting.objects.select_related("address").all()

    if form.is_valid():
        city = form.cleaned_data.get("city")
        price_min = form.cleaned_data.get("price_min")
        price_max = form.cleaned_data.get("price_max")
        rooms_min = form.cleaned_data.get("rooms_min")
        area_min = form.cleaned_data.get("area_min")

        if city:
            lettings_list = lettings_list.filter(
                address__city__icontains=city
            )
        if price_min is not None:
            lettings_list = lettings_list.filter(
                price_per_night__gte=price_min
            )
        if price_max is not None:
            lettings_list = lettings_list.filter(
                price_per_night__lte=price_max
            )
        if rooms_min is not None:
            lettings_list = lettings_list.filter(rooms__gte=rooms_min)
        if area_min is not None:
            lettings_list = lettings_list.filter(area__gte=area_min)

    context = {
        "lettings_list": lettings_list,
        "form": form,
        "result_count": lettings_list.count(),
    }
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Display details for a single letting.

    Retrieves a single Letting by its identifier and renders
    the letting detail page. Raises a 404 error if the letting
    does not exist.

    Args:
        request: HttpRequest object representing the current request.
        letting_id: Primary key of the Letting to display.

    Returns:
        HttpResponse: The rendered letting detail page.
    """
    logger.info("Affichage du letting %s", letting_id)
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
        "letting": letting,
    }
    return render(request, "lettings/letting.html", context)
