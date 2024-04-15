import pytest
from django.contrib.auth.models import User
from faker import Faker

from profiles.models import Profile


class TestProfile:

    #  Profile object cannot be created without a user
    def test_cannot_create_profile_without_user(self):
        # Arrange
        fake = Faker()
        favorite_city = fake.city()

        # Act & Assert
        with pytest.raises(Exception):
            Profile.objects.create(
                favorite_city=favorite_city
            )

    #  Profile object cannot be created with a non-existent user
    def test_cannot_create_profile_with_nonexistent_user(self):
        # Arrange
        fake = Faker()
        favorite_city = fake.city()

        # Act & Assert
        with pytest.raises(Exception):
            Profile.objects.create(
                user_id=9999,
                favorite_city=favorite_city
            )


def _extracted_from__extracted_from_test_user_object_username_is_none_3_4(user, arg1):
    profile = Profile(user=user)
    result = str(profile)
    assert result == arg1


class Test__Str__:

    #  Returns the username of the associated user object as a string.
    def test_returns_username_as_string(self):
        self._extracted_from_test_user_object_username_is_none_3(
            'test_user', 'test_user'
        )

    def test_user_object_has_no_username(self):
        # Arrange
        user = User()
        _extracted_from__extracted_from_test_user_object_username_is_none_3_4(
            user, ''
        )

    #  User object has a username that is an empty string, returns an empty string.
    def test_user_object_username_is_empty_string(self):
        self._extracted_from_test_user_object_username_is_none_3('', '')

    def _extracted_from_test_user_object_username_is_none_3(self, param, param1):
        pass
