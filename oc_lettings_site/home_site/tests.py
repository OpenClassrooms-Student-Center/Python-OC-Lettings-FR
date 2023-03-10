import pytest
from django.test import Client
from django.urls import reverse


@pytest.fixture
def client(db) -> Client:
    return Client()


def test_home_index(client: Client):
    response = client.get(reverse("home:index"), data={})
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in str(response.content)
