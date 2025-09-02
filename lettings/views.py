import logging

from django.http import Http404
from django.shortcuts import render

from lettings.models import Letting

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de toutes les locations.

    Récupère tous les objets Letting depuis la base de données
    et les passe au template 'lettings/index.html' via le contexte.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Affiche le détail d'une location spécifique.

    Utilise l'ID fourni dans l'URL pour récupérer un objet Letting,
    puis transmet son titre et son adresse au template 'lettings/letting.html'.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Letting accédé : {letting.title}, ID: {letting_id}")
    except Letting.DoesNotExist:
        logger.error(f"Letting non trouvé pout l'ID : {letting_id}")
        raise Http404("Letting non trouvé")

    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
