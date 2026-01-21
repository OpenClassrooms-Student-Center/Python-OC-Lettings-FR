import pytest
from django.urls import reverse


class TestOCLettingsSiteURLs:

    @pytest.mark.django_db
    def test_lettings_index_url_success(self, client):
        """
        Test that the lettings index URL is accessible.
        """
        url = reverse('lettings:index')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profiles_url_accessible(self, client):
        """
        Test that the profiles index URL is accessible.
        """
        url = reverse('profiles:index')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_lettings_url_accessible(self, client):
        """
        Test that the lettings URL is accessible.
        """
        url = reverse('lettings:index')
        response = client.get(url)
        assert response.status_code == 200
