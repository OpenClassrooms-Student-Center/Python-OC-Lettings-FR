import pytest
from django.urls import reverse


class TestIndexView:

    @pytest.mark.django_db
    def test_index_view_success(self, client):
        """
        Test that the main index page loads successfully with status code 200.
        """
        url = reverse('index')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_index_view_uses_correct_template(self, client):
        """
        Test that the index view uses the correct template.
        """
        url = reverse('index')
        response = client.get(url)
        assert 'index.html' in [t.name for t in response.templates]

    @pytest.mark.django_db
    def test_index_view_content(self, client):
        """
        Test that the index page displays the expected content.
        """
        url = reverse('index')
        response = client.get(url)
        content = response.content.decode()
        assert 'Welcome to Holiday Homes' in content
        assert 'Profiles' in content
        assert 'Lettings' in content

    @pytest.mark.django_db
    def test_index_view_has_links_to_profiles_and_lettings(self, client):
        """
        Test that the index page contains links to profiles and lettings pages.
        """
        url = reverse('index')
        response = client.get(url)
        content = response.content.decode()
        assert 'href="/profiles/"' in content
        assert 'href="/lettings/"' in content
