from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil du site.

    Rend le template 'index.html' sans contexte particulier.
    """
    return render(request, "index.html")
