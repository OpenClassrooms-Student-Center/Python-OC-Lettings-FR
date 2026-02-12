from django.contrib.auth.models import User
import pytest
from profiles.models import Profile


@pytest.fixture
def sample_profile():
    user_sample = User.objects.create(username="john_doe")
    profile_sample = Profile.objects.create(user=user_sample, favorite_city="Paris")
    return profile_sample


@pytest.fixture
def multiple_profiles():
    """
    Create 3 different profiles for testing.
    Returns a list of Profile objects.
    """
    profiles = []
    for i in range(1, 4):
        user = User.objects.create(username=f"user_{i}")
        profile = Profile.objects.create(user=user, favorite_city=f"City_{i}")
        profiles.append(profile)
    return profiles
