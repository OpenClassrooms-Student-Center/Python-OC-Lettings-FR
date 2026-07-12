"""
Unit tests for the Profile model in profiles.models.

This module verifies:
- The string representation of Profile
- Correct field values
- Relationship with Django User
"""

import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles import views


@pytest.mark.django_db
def test_profile_str(profile):
    """
    Test the string representation of the Profile model.

    The __str__ method should return the username
    of the associated user.
    """
    assert str(profile) == "testuser"


@pytest.mark.django_db
def test_profile_fields(profile, user):
    """
    Test that Profile fields are correctly stored.

    Args:
        profile (Profile): Fixture providing a Profile instance.
        user (User): Fixture providing a User instance.
    """
    assert profile.user == user
    assert profile.favorite_city == "Paris"


@pytest.mark.django_db
def test_profile_user_relationship(profile):
    """
    Test the one-to-one relationship between User and Profile.

    Ensures the related_name 'new_user' works correctly.
    """
    assert profile.user.new_user == profile


"""
URL tests for the profiles application.

This module verifies that URL patterns defined in profiles.urls
correctly resolve to the expected view functions and that
URL reversing works as intended.
"""


@pytest.mark.django_db
def test_profiles_index_url_reverse():
    """
    Test that the profiles index URL is correctly reversed.

    Ensures the 'profiles:profiles_index' named route
    generates the expected URL path.
    """
    url = reverse("profiles:profiles_index")
    assert url == "/profiles/"


@pytest.mark.django_db
def test_profiles_index_url_resolves():
    """
    Test that the profiles index URL resolves
    to the correct view function.
    """
    resolver = resolve("/profiles/")
    assert resolver.func == views.profiles_index


@pytest.mark.django_db
def test_profile_detail_url_reverse():
    """
    Test that the profile detail URL is correctly reversed.

    Ensures the 'profiles:profile' named route generates
    the expected URL when provided with a username.
    """
    url = reverse("profiles:profile", args=["testuser"])
    assert url == "/profiles/testuser/"


@pytest.mark.django_db
def test_profile_detail_url_resolves():
    """
    Test that the profile detail URL resolves
    to the correct view function.
    """
    resolver = resolve("/profiles/testuser/")
    assert resolver.func == views.profile


"""
View tests for the profiles application.

This module verifies that profile-related views return the correct
HTTP responses, use the expected templates, and provide the correct
context data.
"""


@pytest.mark.django_db
def test_profiles_index_view_status_code(client, profile):
    """
    Test that the profiles index view returns HTTP 200.

    Args:
        client (Client): Django test client.
        profile (Profile): Fixture providing a Profile instance.
    """
    response = client.get(reverse("profiles:profiles_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_index_view_template(client, profile):
    """
    Test that the profiles index view uses the correct template.
    """
    response = client.get(reverse("profiles:profiles_index"))
    assert "profiles/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profiles_index_context(client, profile):
    """
    Test that the profiles index view includes profiles in context.
    """
    response = client.get(reverse("profiles:profiles_index"))
    assert "profiles_list" in response.context
    assert profile in response.context["profiles_list"]


@pytest.mark.django_db
def test_profile_detail_view_status_code(client, profile):
    """
    Test that the profile detail view returns HTTP 200
    for an existing profile.
    """
    response = client.get(reverse("profiles:profile", args=[profile.user.username]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_view_template(client, profile):
    """
    Test that the profile detail view uses the correct template.
    """
    response = client.get(reverse("profiles:profile", args=[profile.user.username]))
    assert "profiles/profile.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_detail_context(client, profile):
    """
    Test that the profile detail view passes the correct
    profile object to the template context.
    """
    response = client.get(reverse("profiles:profile", args=[profile.user.username]))
    assert "profile" in response.context
    assert response.context["profile"] == profile


@pytest.mark.django_db
def test_profile_detail_nonexistent_returns_404(client):
    """
    Ensure that requesting a non-existing profile returns HTTP 404.

    The view uses get_object_or_404, so a missing profile should
    result in a 404 response instead of an exception.
    """
    response = client.get(reverse("profiles:profile", args=["unknownuser"]))

    assert response.status_code == 404
    assert "Sorry, the page you are looking for does not exist." in response.content.decode()


"""
Integration tests for the `profiles` Django application.

These tests validate the correct behavior of the profiles application
by exercising the full Django request-response lifecycle:

    URL routing → View execution → Database queries → Template rendering → HTTP response

Unlike unit tests that focus on isolated components such as models
or individual view functions, these integration tests ensure that
multiple layers of the application interact correctly when accessed
through HTTP requests.

The tests cover several categories of behavior:

Happy paths:
    - Accessing the profiles index page successfully
    - Rendering existing profiles in the index page
    - Navigating to a specific profile page
    - Displaying profile details retrieved from the database

Edge cases:
    - Handling situations where no profiles exist

Sad paths (Test-Driven Development approach):
    - Requesting a profile that does not exist should return HTTP 404
    - Requesting a user without an associated profile should return HTTP 404

Some tests intentionally document expected behaviors that may not yet
be implemented in the application. These tests may initially fail
until proper error handling is introduced (for example using
Django's `get_object_or_404` helper).

This follows a Test-Driven Development (TDD) approach where expected
application behavior is specified before implementing the logic.
"""


@pytest.mark.django_db
def test_profiles_index_page_accessible(client):
    """
    Verify that the profiles index page is accessible.

    This test ensures that the URL associated with the profiles
    index view resolves correctly and returns a valid HTTP response.

    The test validates that:
        - the URL can be generated using Django's reverse function
        - the view returns HTTP status code 200
        - the request completes without errors

    This confirms that URL routing, view execution, and template
    rendering are correctly integrated.
    """
    url = reverse("profiles:profiles_index")

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_index_uses_correct_template(client):
    """
    Verify that the profiles index view renders the correct template.

    The view should render the 'profiles/index.html' template.
    This test ensures that the template layer is correctly
    connected to the view logic.
    """
    url = reverse("profiles:profiles_index")

    response = client.get(url)

    templates = [t.name for t in response.templates]

    assert "profiles/index.html" in templates


@pytest.mark.django_db
def test_profiles_index_displays_existing_profiles(client, profile):
    """
    Verify that existing profiles are displayed on the index page.

    This test creates a Profile instance using a fixture and ensures
    that the username associated with the profile appears in the
    rendered HTML response.

    This confirms that:
        - profiles are correctly retrieved from the database
        - the context variable `profiles_list` is passed to the template
        - the template correctly renders profile usernames.
    """
    url = reverse("profiles:profiles_index")

    response = client.get(url)

    content = response.content.decode()

    assert profile.user.username in content


@pytest.mark.django_db
def test_profiles_index_handles_empty_dataset(client):
    """
    Verify the behavior of the index page when no profiles exist.

    If the database contains no Profile instances, the template
    should display a fallback message informing the user that
    no profiles are available.

    This ensures the application handles empty datasets gracefully.
    """
    url = reverse("profiles:profiles_index")

    response = client.get(url)

    content = response.content.decode()

    assert response.status_code == 200
    assert "No profiles are available." in content


@pytest.mark.django_db
def test_profile_detail_page_accessible(client, profile):
    """
    Verify that the profile detail page is accessible for an existing user.

    This test ensures that the dynamic URL using the username parameter
    resolves correctly and retrieves the associated profile.

    The test validates that:
        - the URL is correctly generated with reverse()
        - the view returns HTTP status code 200
        - the profile template is used for rendering the response.
    """
    url = reverse("profiles:profile", args=[profile.user.username])

    response = client.get(url)

    assert response.status_code == 200
    assert "profiles/profile.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_detail_displays_user_information(client, profile):
    """
    Verify that the profile detail page displays user information.

    The template should render fields associated with the User model
    as well as the Profile model itself.

    This test ensures that the following data appears in the response:
        - username
        - favorite city

    This confirms the correct integration between the Profile model,
    the related User model, the view logic, and the template rendering.
    """
    url = reverse("profiles:profile", args=[profile.user.username])

    response = client.get(url)

    content = response.content.decode()

    assert profile.user.username in content
    assert profile.favorite_city in content


@pytest.mark.django_db
def test_profile_detail_returns_404_for_unknown_username(client):
    """
    Verify that requesting a profile with an unknown username
    returns HTTP 404.

    According to standard web application behavior, requesting
    a resource that does not exist should return a 404 response.

    This test documents the expected behavior of the application
    when the requested profile does not exist in the database.

    The current implementation may raise an unhandled exception
    which results in a 500 error. This test follows a
    Test-Driven Development approach and will pass once proper
    error handling is implemented.
    """
    url = reverse("profiles:profile", args=["unknown_user"])

    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_profile_detail_user_without_profile_returns_404(client):
    """
    Verify that requesting a user without an associated profile
    returns HTTP 404.

    In some cases a Django User may exist without a corresponding
    Profile instance. The application should handle this situation
    gracefully and return a 404 response rather than raising an
    unhandled exception.

    This test documents the expected behavior and may initially
    fail until proper error handling is implemented in the view.
    """
    user = User.objects.create(username="orphan_user")

    url = reverse("profiles:profile", args=[user.username])

    response = client.get(url)

    assert response.status_code == 404
    assert "Sorry, the page you are looking for does not exist." in response.content.decode()
