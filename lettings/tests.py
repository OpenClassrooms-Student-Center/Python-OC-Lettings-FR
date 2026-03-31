"""Tests for the lettings application views.

This module contains integration tests for the lettings index
and detail views, verifying HTTP status codes, rendered templates
and expected content.
"""

import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_view(client):
    """Test the lettings index view.

    This test ensures that the lettings index page:
    - returns a 200 HTTP status code,
    - displays the created letting title,
    - renders the expected template.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    address = Address.objects.create(
        number=1,
        street="Main Street",
        city="City",
        state="ST",
        zip_code="12345",
        country_iso_code="USA",
    )
    Letting.objects.create(title="Test Letting", address=address)

    url = reverse("lettings:index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Test Letting" in response.content.decode()
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_letting_detail_view(client):
    """Test the letting detail view.

    This test ensures that the letting detail page:
    - returns a 200 HTTP status code,
    - displays the correct letting title,
    - renders the expected template.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    address = Address.objects.create(
        number=2,
        street="Second Street",
        city="City",
        state="ST",
        zip_code="67890",
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="Detail Letting", address=address)

    url = reverse("lettings:letting", kwargs={"letting_id": letting.id})
    response = client.get(url)

    assert response.status_code == 200
    assert "Detail Letting" in response.content.decode()
    assert "lettings/letting.html" in [t.name for t in response.templates]
