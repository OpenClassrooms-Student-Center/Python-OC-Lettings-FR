import pytest

from django.core.management import call_command
from django.urls import reverse


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'data.json')


@pytest.mark.django_db
def test_index_profiles_get(client):
    response = client.get(reverse('profiles:index'))
    assert b'<title>Profiles</title>' in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_get(client):
    response = client.get(reverse('profiles:profile', args=["HeadlinesGazer"]))
    assert b"<h1>HeadlinesGazer</h1>" in response.content
    assert response.status_code == 200
