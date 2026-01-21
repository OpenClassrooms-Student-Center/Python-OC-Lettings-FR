from django.urls import reverse
import pytest


class TestProfilesURLs:

    @pytest.mark.django_db
    def test_profile_index_url_success(self, client):
        """
        Test that the profile index URL resolves correctly.
        """
        url = reverse('profiles:index')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profile_index_empty_list(self, client):
        """
        Test that the profile index URL displays an empty list message when no profiles exist.
        """
        url = reverse('profiles:index')
        response = client.get(url)
        assert response.status_code == 200
        assert "No profiles are available." in response.content.decode()


class TestProfileDetailURL:

    @pytest.mark.django_db
    def test_profile_detail_url_success(self, client, sample_profile):
        """
        Test that the profile detail URL resolves correctly.
        """
        url = reverse('profiles:profile', args=[sample_profile.user.username])
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profile_detail_not_found(self, client):
        """
        Test that a non-existent profile returns a 404 status code.
        """
        url = reverse('profiles:profile', args=['non_existent_user'])
        response = client.get(url)
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_profile_detail_uses_correct_template(self, client, sample_profile):
        """
        Test that the profile detail URL uses the correct template.
        """
        url = reverse('profiles:profile', args=[sample_profile.user.username])
        response = client.get(url)
        assert 'profiles/profile.html' in [t.name for t in response.templates]
        assert sample_profile.user.username in response.content.decode()
