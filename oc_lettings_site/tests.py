"""Tests for the home page view of the OC Lettings site.

This module verifies that the index view is reachable and renders
the expected content and template.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_index_view_status_code(client):
    user = User.objects.create_user(username="testuser", password="Testpass123!")
    client.force_login(user)

    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Orange County Lettings" in response.content.decode()


@pytest.mark.django_db
def test_index_view_template(client):
    """Test that the index view renders the correct template.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("index")
    response = client.get(url)

    assert "index.html" in [t.name for t in response.templates]
