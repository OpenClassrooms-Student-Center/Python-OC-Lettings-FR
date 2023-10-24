from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse, resolve
from profiles.models import Profile


class ProfilesUrlsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="test_user_name")

    def test_profile_index_url(self):
        Profile.objects.create(
            user=self.user,
            favorite_city="My favorite city")
        path = reverse('profiles:index')

        assert path == "/profiles/"
        assert resolve(path).view_name == "profiles:index"

    def test_profile_url(self):
        profile = Profile.objects.create(
            user=self.user,
            favorite_city="My favorite city")
        path = reverse('profiles:profile', args=[profile.user.username])
        assert path == "/profiles/test_user_name/"
        assert resolve(path).view_name == "profiles:profile"
