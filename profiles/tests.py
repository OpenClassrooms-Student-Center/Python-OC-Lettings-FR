"""Tests for the profiles application views.

This module contains integration tests for the profiles index
and detail views, verifying status codes, rendered templates
and expected content.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    user = User.objects.create_user(username="john")
    Profile.objects.create(user=user)

    client.force_login(user)

    url = reverse("profiles:index")
    response = client.get(url, follow=True)

    assert response.status_code == 200
    assert "john" in response.content.decode()


@pytest.mark.django_db
def test_profile_detail_view(client):
    """Test the profile detail view.

    Ensures that the profile detail page:
    - returns a 200 HTTP status code,
    - displays the correct username,
    - renders the expected template.
    """
    # Création utilisateur + profil
    user = User.objects.create_user(username="jane", password="Testpass123!")
    profile = Profile.objects.create(user=user)

    # 🔥 Connexion forcée
    client.force_login(user)

    # Appel de la vue
    url = reverse("profiles:profile", kwargs={"username": profile.user.username})
    response = client.get(url)

    # Vérifications
    assert response.status_code == 200
    assert "profiles/profile.html" in [t.name for t in response.templates]
    assert response.context["profile"].user.username == "jane"
