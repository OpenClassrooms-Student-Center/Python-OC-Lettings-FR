import pytest
from django.contrib.auth.models import User

from django.urls import reverse, resolve
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_url():
    """Test the URL routing for user profiles.

    This test verifies that the URL for a user's profile is generated correctly
    and that it resolves to the expected view function.

    Database setup:
        - Creates a User instance with a specific username.
        - Creates a Profile instance associated with the created User.

    Steps:
        - Generates the URL for the user's profile using the username.
        - Checks if the generated URL matches the expected format.
        - Resolves the URL and verifies that the associated view name is correct.

    Assertions:
        - Verifies that the generated URL matches '/profiles/{username}/'.
        - Verifies that the resolved view name is 'profiles:profile'.
    """

    user = User.objects.create_user(username='4meRomance', password='password')
    Profile.objects.create(id=1, favorite_city="Marseille", user_id=user.id)

    path = reverse('profiles:profile', kwargs={'username': user.username})

    assert path == "/profiles/4meRomance/"
    assert resolve(path).view_name == 'profiles:profile'
