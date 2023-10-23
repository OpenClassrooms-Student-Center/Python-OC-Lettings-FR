from django.test import TestCase

from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesModelsTestCase(TestCase):

    def test_profile_model(self):
        user = User.objects.create(username="test_user_name")
        profile = Profile.objects.create(
                user=user,
                favorite_city="My favorite city")
        expected_value = "test_user_name"
        assert str(profile) == expected_value
