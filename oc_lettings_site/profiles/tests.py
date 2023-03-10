import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from .models import Profile


@pytest.fixture
def client(db) -> Client:
    return Client()


@pytest.fixture
def user_test(db):
    return User.objects.create_user(username="User1", password="pwd12345")


@pytest.fixture
def profile_test(db, user_test: User):
    return Profile.objects.create(user=user_test, favorite_city="Paris")


def test_index_profile(client: Client):
    response = client.get(reverse("profiles:index"), data={})
    assert response.status_code == 200
    assert "<title>Profiles</title>" in str(response.content)


def test_details_profile(client: Client, profile_test: Profile):
    response = client.get(reverse("profiles:profile", args=["User1"]), data={})
    assert response.status_code == 200
    assert "<title>User1</title>" in str(response.content)


def test_str_profile(profile_test: Profile):
    assert str(profile_test) == "User1"
