from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

import pytest

from profiles.models import Profile

c = Client()


@pytest.mark.django_db
def test_profile_index_uri():
    c = Client()
    profile_index_uri = reverse('profiles_index')
    resp = c.get(profile_index_uri)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_profile_index_title():
    c = Client()
    profile_index_uri = reverse('profiles_index')
    resp = c.get(profile_index_uri)
    assert b"<title>" in resp.content


@pytest.mark.django_db
def test_profile_uri():
    c = Client()

    new_user = User.objects.create_user(username='testuser', password='1234')
    profile = Profile.objects.create(
        user=new_user,
        favorite_city="p$aozd"
    )

    profile_uri = reverse('profile', args=['testuser'])
    resp = c.get(profile_uri)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_profile_title():
    c = Client()

    new_user = User.objects.create_user(username='testuser', password='1234')
    profile = Profile.objects.create(
        user=new_user,
        favorite_city="p$aozd"
    )

    profile_uri = reverse('profile', args=['testuser'])
    resp = c.get(profile_uri)
    assert b"<title>" in resp.content
