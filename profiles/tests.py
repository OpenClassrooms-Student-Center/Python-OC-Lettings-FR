from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class ProfilesTest(TestCase):
    def test_view_code(self):
        response = self.client.get(reverse('profiles:index'))
        assert response.status_code == 200

    def test_view_title(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, "Profiles")

    def test_particular_profile(self):
        user = User.objects.create_user("userTest", "user@test.com", "mOtDePaSsE124")
        Profile.objects.create(user=user, favorite_city="Bordeaux")
        response = self.client.get(reverse("profiles:profile", kwargs={"username":"userTest"}))
        self.assertContains(response, "userTest")