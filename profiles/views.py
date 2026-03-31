"""Views for the profiles application.

This module contains views responsible for displaying the list
of user profiles and the details of a single profile, with
logging for basic monitoring.
"""

import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from profiles.models import Profile
from profiles.forms import TenantProfileForm

logger = logging.getLogger(__name__)


def is_admin(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_admin, login_url="/accounts/login/")
def index(request):
    logger.info("Affichage de la liste des profils par %s", request.user.username)
    profiles = Profile.objects.select_related("user").filter(user__is_active=True)
    context = {"profiles_list": profiles}
    return render(request, "profiles/index.html", context)


@login_required
def profile(request, username):
    """Accessible par le propriétaire ou un admin.
    Si le profil n'existe pas encore, redirige vers edit."""

    # Un utilisateur ne peut voir que son propre dossier (sauf admin)
    if request.user.username != username and not request.user.is_staff:
        return redirect("profiles:profile", username=request.user.username)

    # Crée le profil s'il n'existe pas encore au lieu de faire 404
    profile, created = Profile.objects.get_or_create(
        user__username=username,
        defaults={"user": request.user}
    )

    # Si le profil vient d'être créé, envoie directement vers edit
    if created:
        return redirect("profiles:edit")

    logger.info("Affichage du profil pour %s", username)
    return render(request, "profiles/profile.html", {"profile": profile})


@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = TenantProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            logger.info("Dossier mis à jour pour %s", request.user.username)
            return redirect("profiles:profile", username=request.user.username)
    else:
        form = TenantProfileForm(instance=profile)
    return render(request, "profiles/edit_profile.html", {"form": form})
