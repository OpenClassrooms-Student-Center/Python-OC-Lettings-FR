import pytest


class TestProfileModel:

    @pytest.mark.django_db
    def test_profile_str(self, sample_profile):
        """
        Test the string representation of the Profile model.
        """
        assert str(sample_profile) == "john_doe"
        assert sample_profile.favorite_city == "Paris"
