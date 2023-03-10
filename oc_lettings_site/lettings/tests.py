import pytest
from django.test import Client
from django.urls import reverse

from .models import Address, Letting


@pytest.fixture
def client(db) -> Client:
    return Client()


@pytest.fixture
def test_address(db):
    return Address.objects.create(
        number=1,
        street="my street",
        city="my city",
        state="France",
        zip_code="75001",
        country_iso_code="FRA",
    )


@pytest.fixture
def test_letting(db, test_address):
    return Letting.objects.create(title="My vacation home", address=test_address)


def test_index_lettings(client: Client):
    response = client.get(reverse("lettings:index"), data={})
    assert response.status_code == 200
    assert "<title>Lettings</title>" in str(response.content)


def test_detail_letting(client: Client, test_letting: Letting):
    response = client.get(reverse("lettings:letting", args=[1]), data={})
    assert response.status_code == 200
    assert "My vacation home" in str(response.content)


def test_str_letting(test_letting: Letting):
    assert str(test_letting) == "My vacation home"


def test_str_address(test_address: Address):
    assert str(test_address) == "1 my street"
