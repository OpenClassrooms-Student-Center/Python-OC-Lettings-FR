"""
Models for the profiles application.

This module defines the Profile model, which extends the built-in
Django User model with additional application-specific data,
such as the user's favorite city.
"""

import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def user():
    """
    Fixture that creates a sample Django User instance.

    Returns:
        User: A saved User instance with test credentials.
    """
    return User.objects.create(username="testuser")


@pytest.fixture
def profile(user):
    """
    Fixture that creates a sample Profile instance linked to a User.

    Args:
        user (User): Fixture providing a User instance.

    Returns:
        Profile: A saved Profile instance with sample data.
    """
    return Profile.objects.create(user=user, favorite_city="Paris")
