import pytest
from django.urls import reverse


class TestLettingsView:

    @pytest.mark.django_db
    def test_index_view_success(self, client, multiple_lettings):
        """
        Test that the lettings index page loads successfully.
        """
        url = reverse('lettings:index')
        response = client.get(url)
        content = response.content.decode()
        assert content.count('<li class="list-group-item">') == 3
        assert "Cozy Cottage 1" in content
        assert "Cozy Cottage 2" in content
        assert "Cozy Cottage 3" in content

    @pytest.mark.django_db
    def test_index_view_empty_list(self, client):
        """
        Test that the index page displays a message when no lettings are available.
        """
        url = reverse('lettings:index')
        response = client.get(url)
        content = response.content.decode()
        assert 'No lettings are available.' in content

    @pytest.mark.django_db
    def test_lettings_index_uses_correct_template(self, client, sample_letting):
        """
        Test that the index view uses the correct template.
        """
        url = reverse('lettings:index')
        response = client.get(url)
        assert 'lettings/index.html' in [t.name for t in response.templates]
        assert sample_letting.title in response.content.decode()

    @pytest.mark.django_db
    def test_lettings_index_content(self, client, sample_letting):
        """
        Test that the lettings index page displays the title of the letting.
        """
        url = reverse('lettings:index')
        response = client.get(url)
        assert sample_letting.title in response.content.decode()

    @pytest.mark.django_db
    def test_letting_detail_view_success(self, client, sample_letting):
        """
        Test that the letting detail page loads successfully.
        """
        url = reverse('lettings:letting', args=[sample_letting.id])
        response = client.get(url)
        content = response.content.decode()
        assert sample_letting.title in content
        assert sample_letting.address.__str__() in content

    @pytest.mark.django_db
    def test_letting_detail_content(self, client, sample_letting):
        """
        Test that the letting detail page displays the title and address.
        """
        url = reverse('lettings:letting', args=[sample_letting.id])
        response = client.get(url)
        content = response.content.decode()
        assert sample_letting.title in content
        assert str(sample_letting.address) in content

    @pytest.mark.django_db
    def test_letting_detail_uses_correct_template(self, client, sample_letting):
        """
        Test that the detail view uses the correct template.
        """
        url = reverse('lettings:letting', args=[sample_letting.id])
        response = client.get(url)
        assert 'lettings/letting.html' in [t.name for t in response.templates]
