"""Tests for the accounts application.

This module contains integration tests for the signup, login,
logout and profile views, verifying HTTP status codes,
redirections, rendered templates and authentication state.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_signup_view_get(client):
    """Test that the signup page renders correctly.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("accounts:signup")
    response = client.get(url)

    assert response.status_code == 200
    assert "accounts/signup.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_signup_view_post_valid(client):
    """Test that a valid signup creates a user and redirects.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("accounts:signup")
    data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password1": "Testpass123!",
        "password2": "Testpass123!",
    }
    response = client.post(url, data)

    assert response.status_code == 302
    assert User.objects.filter(username="newuser").exists()


@pytest.mark.django_db
def test_signup_view_post_invalid(client):
    """Test that mismatched passwords re-render the signup form with errors.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("accounts:signup")
    data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password1": "Testpass123!",
        "password2": "WrongPass456!",
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert not User.objects.filter(username="newuser").exists()


@pytest.mark.django_db
def test_signup_redirects_if_authenticated(client):
    """Test that an already authenticated user is redirected from signup.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    User.objects.create_user(username="existing", password="Testpass123!")
    client.login(username="existing", password="Testpass123!")

    url = reverse("accounts:signup")
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_login_view_get(client):
    """Test that the login page renders correctly.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("accounts:login")
    response = client.get(url)

    assert response.status_code == 200
    assert "accounts/login.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_login_view_post_valid(client):
    """Test that valid credentials log the user in and redirect.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    User.objects.create_user(username="testuser", password="Testpass123!")

    url = reverse("accounts:login")
    response = client.post(url, {
        "username": "testuser",
        "password": "Testpass123!",
    })

    assert response.status_code == 302


@pytest.mark.django_db
def test_login_view_post_invalid(client):
    """Test that invalid credentials re-render the login form.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("accounts:login")
    response = client.post(url, {
        "username": "ghost",
        "password": "wrongpass",
    })

    assert response.status_code == 200
    assert "accounts/login.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_login_redirects_if_authenticated(client):
    """Test that an already authenticated user is redirected from login.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    User.objects.create_user(username="testuser", password="Testpass123!")
    client.login(username="testuser", password="Testpass123!")

    url = reverse("accounts:login")
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_view(client):
    """Test that logout logs the user out and redirects to home.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    User.objects.create_user(username="testuser", password="Testpass123!")
    client.login(username="testuser", password="Testpass123!")

    url = reverse("accounts:logout")
    response = client.post(url)

    assert response.status_code == 302
    assert response.url == reverse("index")


@pytest.mark.django_db
def test_profile_view_authenticated(client):
    """Test that an authenticated user can access their profile page.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="Testpass123!"
    )
    client.login(username="testuser", password="Testpass123!")

    url = reverse("accounts:profile")
    response = client.get(url)

    assert response.status_code == 200
    assert "accounts/profile.html" in [t.name for t in response.templates]
    assert "testuser" in response.content.decode()


@pytest.mark.django_db
def test_profile_view_unauthenticated(client):
    """Test that an unauthenticated user is redirected from the profile page.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("accounts:profile")
    response = client.get(url)

    assert response.status_code == 302
    assert "/accounts/login/" in response.url
