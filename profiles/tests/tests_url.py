"""
Tests module for profiles app urls
"""
import pytest

from django.contrib.auth.models import User
from django.urls import reverse, resolve

from profiles.models import Profile


class TestProfilesUrl:
    def test_profiles_index_url(self):
        """
        Method to test that the profiles index url works
        """
        path = reverse("profiles:index")

        assert path == "/profiles/"
        assert resolve(path).view_name == 'profiles:index'

    @pytest.mark.django_db
    def test_profiles_profile_url(self):
        """
        Method to test that the profiles profile url works
        """
        Profile.objects.create(user=User.objects.create_user(username="Username",
                                                             first_name='First Name',
                                                             last_name='Last Name',
                                                             email='test@test.com'),
                               favorite_city="Paris")

        path = reverse(viewname="profiles:profile", kwargs={'username': "Username"})

        assert path == "/profiles/Username/"
        assert resolve(path).view_name == "profiles:profile"
