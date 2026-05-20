import pytest

from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def get_profile():
    """
    Fixture that returns fictive profile
    Returns:
        The profile object
    """
    return Profile.objects.create(
        user=User.objects.create_user(username='Username',
                                      first_name='First',
                                      last_name='Last',
                                      email='test@test.com',
                                      password='test_pwd'),
        favorite_city="City Test"
    )
