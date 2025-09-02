import logging

from django.http import Http404
from django.shortcuts import render

from profiles.models import Profile

# Create your views here.


logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de tous les profils clients.

    Récupère tous les objets Profile de la base de données et les transmet
    au template 'profiles/index.html' via le contexte.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Affiche le détail d’un profil client à partir du nom d’utilisateur.

    Utilise le nom d'utilisateur fourni dans l'URL pour retrouver
    le profil associé via la relation au modèle User, et transmet
    cet objet au template 'profiles/profile.html'.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Profile consulté : {username}")
    except Profile.DoesNotExist:
        logger.error(f"Profile introuvable pour l'utilisateur: {username}")
        raise Http404("profile non trouvé")

    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
