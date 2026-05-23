"""
Tests module for profiles app models
"""
import pytest

from profiles.models import Profile


class TestProfilesModel:
    @pytest.mark.django_db
    def test_profiles_profile_model_ok(self, get_profile: Profile):
        expected = f"{get_profile.user.username}"

        assert str(get_profile) == expected
