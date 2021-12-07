import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_profile_index(client):
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200