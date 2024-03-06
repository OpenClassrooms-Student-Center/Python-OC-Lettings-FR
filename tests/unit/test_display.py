from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


# comment
def test_get_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')


@pytest.mark.django_db
def test_get_lettings_index(client, django_db_setup):
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_get_profiles_index(client):
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_get_letting_with_id(client, django_db_setup):
    response = client.get(reverse('letting', kwargs={'letting_id': 1}), follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')


@pytest.mark.django_db
def test_get_profile(client, django_db_setup):
    response = client.get(reverse('profile', args=("HeadlinesGazer",)), follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')


@pytest.mark.django_db
def test_500_get_wrong_letting(client, django_db_setup):
    response = client.get(reverse('letting', kwargs={'letting_id': 100}), follow=True)
    assert response.status_code == 500


@pytest.mark.django_db
def test_404(client):
    response = client.get("idont_exits")
    assert response.status_code == 404
