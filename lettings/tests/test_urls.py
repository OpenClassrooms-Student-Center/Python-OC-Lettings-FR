from django.urls import reverse
import pytest


class TestLettingsUrls:

    @pytest.mark.django_db
    def test_lettings_index_success(self, client):
        """
        Test that the lettings index page loads successfully.
        """
        url = reverse('lettings:index')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_letting_detail_success(self, client, sample_letting):
        """
        Test that the letting detail page loads successfully.
        """
        url = reverse('lettings:letting', args=[sample_letting.id])
        response = client.get(url)
        assert response.status_code == 200
