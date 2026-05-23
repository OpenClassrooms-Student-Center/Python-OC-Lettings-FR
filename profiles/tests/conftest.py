"""
Fixture module for profiles tests
"""
import pytest

from _pytest.monkeypatch import MonkeyPatch
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture(autouse=True)
def disable_sentry(monkeypatch: MonkeyPatch):
    monkeypatch.setattr(
        "monitoring.sentry_sdk.init",
        lambda *args, **kwargs: None
    )


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
