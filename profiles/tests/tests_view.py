"""
Tests module for profiles app views
"""
import pytest

from django.urls import reverse
from django.test import Client, override_settings
from pytest_django.asserts import assertTemplateUsed
from _pytest.monkeypatch import MonkeyPatch

from profiles.models import Profile


class TestProfilesView:
    @pytest.mark.django_db
    def test_profiles_index_view_ok(self, get_profile: Profile):
        """
        Method to test the profiles index view
        Args:
            get_profile (Profile): a Profile object
        """
        client = Client()
        path = reverse(viewname="profiles:index")

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = "Profiles"
        expected_content = (f'<a href="/profiles/{get_profile.user.username}/">'
                            f'{get_profile.user.username}</a>')

        assert expected_h1 in content
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, template_name="profiles/index.html")

    @pytest.mark.django_db
    def test_profiles_index_view_returns_500(self, monkeypatch: MonkeyPatch, get_profile: Profile):
        """
        Method to test that the profiles index view returns 500 in case of 500 error
        Args:
            monkeypatch (MonkeyPatch): a MonkeyPatch object
            get_profile (Profile): a Profile object
        """
        def raise_error():
            raise Exception("forced error")

        monkeypatch.setattr("profiles.views.Profile.objects.all", raise_error)

        client = Client()
        client.raise_request_exception = False
        path = reverse(viewname="profiles:index")

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = f"Internal Error : something wrong with the server !"

        assert expected_h1 in content
        assert response.status_code == 500
        assertTemplateUsed(response, template_name="oc_lettings_site/500.html")

    @pytest.mark.django_db
    def test_profiles_profile_view_ok(self, get_profile: Profile):
        """
        Method to test that the profiles profile view returns 200
        Args:
            get_profile (Profile): a Profile object
        """
        client = Client()
        path = reverse(viewname="profiles:profile", kwargs={"username": get_profile.user.username})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = f"{get_profile.user.username}"
        expected_content = [f'<strong>First name :</strong> {get_profile.user.first_name}',
                            f'<strong>Last name :</strong> {get_profile.user.last_name}',
                            f'<strong>Email :</strong> {get_profile.user.email}',
                            f'<strong>Favorite city :</strong> {get_profile.favorite_city}']

        assert expected_h1 in content
        for expected_child in expected_content:
            assert expected_child in content
        assert response.status_code == 200
        assertTemplateUsed(response, template_name="profiles/profile.html")

    @override_settings(DEBUG=False)
    @pytest.mark.django_db
    def test_profiles_profile_view_returns_404(self, get_profile: Profile):
        """
        Method to test that the profiles profile view returns 404 in case of 404 error
        Args:
            get_profile (Profile): a Profile object
        """
        client = Client()
        path = reverse(viewname="profiles:profile", kwargs={"username": "test"})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = f"404 Error : profile \'test\' not found !"

        assert expected_h1 in content
        assert response.status_code == 404
        assertTemplateUsed(response, template_name="oc_lettings_site/404.html")

    @pytest.mark.django_db
    def test_profiles_profile_view_returns_500(self,
                                               monkeypatch: MonkeyPatch,
                                               get_profile: Profile):
        """
        Method to test that the profiles profile view returns 500 in case of 500 error
        Args:
            monkeypatch (MonkeyPatch): a MonkeyPatch object
            get_profile (Profile): a Profile object
        """
        def raise_error(*args, **kwargs):
            raise Exception("forced error")

        monkeypatch.setattr("profiles.views.get_object_or_404", raise_error)

        client = Client()
        client.raise_request_exception = False
        path = reverse(viewname="profiles:profile", kwargs={"username": get_profile.user.username})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = f"Internal Error : something wrong with the server !"

        assert expected_h1 in content
        assert response.status_code == 500
        assertTemplateUsed(response, template_name="oc_lettings_site/500.html")
