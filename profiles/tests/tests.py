"""
Tests module for profiles app
"""
import pytest

from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from _pytest.monkeypatch import MonkeyPatch

from profiles.models import Profile


class TestProfilesUrl:
    def test_profiles_index_url(self):
        path = reverse("profiles:index")

        assert path == "/profiles/"
        assert resolve(path).view_name == 'profiles:index'

    @pytest.mark.django_db
    def test_profiles_profile_url(self):
        Profile.objects.create(user=User.objects.create_user(username="Username",
                                                             first_name='First Name',
                                                             last_name='Last Name',
                                                             email='test@test.com'),
                               favorite_city="Paris")

        path = reverse(viewname="profiles:profile", kwargs={'username': "Username"})

        assert path == "/profiles/Username/"
        assert resolve(path).view_name == "profiles:profile"


class TestProfilesView:
    @pytest.mark.django_db
    def test_profiles_index_view_ok(self, get_profile: Profile):
        client = Client()
        path = reverse(viewname="profiles:index")

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = '<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>'
        expected_content = (f'<a href="/profiles/{get_profile.user.username}/">'
                            f'{get_profile.user.username}</a>')

        assert expected_h1 in content
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, template_name="profiles/index.html")

    @pytest.mark.django_db
    def test_profiles_index_view_returns_500(self, monkeypatch: MonkeyPatch, get_profile: Profile):
        def raise_error():
            raise Exception("forced error")

        monkeypatch.setattr("profiles.views.Profile.objects.all", raise_error)

        client = Client()
        path = reverse(viewname="profiles:index")

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = (f'<h1 class="page-header-ui-title mb-3 display-6">500 Error : '
                       f'something wrong with the server - forced error</h1>')

        assert expected_h1 in content
        assert response.status_code == 500
        assertTemplateUsed(response, template_name="error_500.html")

    @pytest.mark.django_db
    def test_profiles_profile_view_ok(self, get_profile: Profile):
        client = Client()
        path = reverse(viewname="profiles:profile", kwargs={"username": get_profile.user.username})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = (f'<h1 class="page-header-ui-title mb-3 display-6">'
                       f'{get_profile.user.username}</h1>')
        expected_content = (f'<p><strong>First name :</strong> {get_profile.user.first_name}'
                            f'</p>\n\t\t\t'
                            f'<p><strong>Last name :</strong> {get_profile.user.last_name}'
                            f'</p>\n\t\t\t'
                            f'<p><strong>Email :</strong> {get_profile.user.email}</p>\n\t\t\t'
                            f'<p><strong>Favorite city :</strong> {get_profile.favorite_city}</p>')

        assert expected_h1 in content
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, template_name="profiles/profile.html")

    @pytest.mark.django_db
    def test_profiles_profile_view_returns_404(self, get_profile: Profile):
        client = Client()
        path = reverse(viewname="profiles:profile", kwargs={"username": "test"})

        response = client.get(path=path)
        content = response.content.decode()

        expected_h1 = (f'<h1 class="page-header-ui-title mb-3 display-6">404 Error : '
                       f'profile \'test\' not found !</h1>')

        assert expected_h1 in content
        assert response.status_code == 404
        assertTemplateUsed(response, template_name="error_404.html")

    @pytest.mark.django_db
    def test_profiles_profile_view_returns_500(self,
                                               monkeypatch: MonkeyPatch,
                                               get_profile: Profile):
        def raise_error(*args, **kwargs):
            raise Exception("forced error")

        monkeypatch.setattr("profiles.views.Profile.objects.get", raise_error)

        client = Client()
        path = reverse(viewname="profiles:profile", kwargs={"username": get_profile.user.username})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = (f'<h1 class="page-header-ui-title mb-3 display-6">500 Error : '
                       f'something wrong with the server - forced error</h1>')

        assert expected_h1 in content
        assert response.status_code == 500
        assertTemplateUsed(response, template_name="error_500.html")


class TestProfilesModel:
    @pytest.mark.django_db
    def test_profiles_profile_model_ok(self, get_profile: Profile):
        expected = f"{get_profile.user.username}"

        assert str(get_profile) == expected
