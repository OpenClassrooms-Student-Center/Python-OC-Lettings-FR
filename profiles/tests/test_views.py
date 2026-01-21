import pytest
from django.urls import reverse


class TestProfileView:

    @pytest.mark.django_db
    def test_index_view_success(self, client, multiple_profiles):
        """
        Test that the profile index view loads successfully.
        """
        url = reverse('profiles:index')
        response = client.get(url)
        content = response.content.decode()
        assert content.count('<li class="list-group-item">') == 3
        assert "user_1" in content
        assert "user_2" in content
        assert "user_3" in content

    @pytest.mark.django_db
    def test_index_view_empty_list(self, client):
        """
        Test that the profile index view displays a message when no profiles are available.
        """
        url = reverse('profiles:index')
        response = client.get(url)
        content = response.content.decode()
        assert 'No profiles are available.' in content

    @pytest.mark.django_db
    def test_profile_index_url_uses_correct_template(self, client):
        """
        Test that the profile index URL uses the correct template.
        """
        url = reverse('profiles:index')
        response = client.get(url)
        assert 'profiles/index.html' in [t.name for t in response.templates]

    @pytest.mark.django_db
    def test_profile_index_content(self, client, sample_profile):
        """
        Test that the profile index page displays the username of the profile.
        """
        url = reverse('profiles:index')
        response = client.get(url)
        assert sample_profile.user.username in response.content.decode()

    @pytest.mark.django_db
    def test_profile_detail_view_success(self, client, sample_profile):
        """
        Test that the profile detail page loads successfully.
        """
        url = reverse('profiles:profile', args=[sample_profile.user.username])
        response = client.get(url)
        content = response.content.decode()
        assert sample_profile.user.username in content
        assert sample_profile.favorite_city in content

    @pytest.mark.django_db
    def test_profile_detail_content(self, client, sample_profile):
        """
        Test that the profile detail page displays the correct profile information.
        """
        url = reverse('profiles:profile', args=[sample_profile.user.username])
        response = client.get(url)
        content = response.content.decode()
        assert sample_profile.user.username in content
        assert sample_profile.favorite_city in content

    @pytest.mark.django_db
    def test_profile_detail_uses_correct_template(self, client, sample_profile):
        """
        Test that the profile detail view uses the correct template.
        """
        url = reverse('profiles:profile', args=[sample_profile.user.username])
        response = client.get(url)
        assert 'profiles/profile.html' in [t.name for t in response.templates]
