"""Tests for the contact application.

This module contains integration tests for the contact form view,
verifying HTTP status codes, rendered templates, form validation
and email sending behaviour.
"""

import pytest
from django.urls import reverse
from django.core import mail


@pytest.mark.django_db
def test_contact_view_get(client):
    """Test that the contact page renders correctly.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("contact:contact")
    response = client.get(url)

    assert response.status_code == 200
    assert "contact/contact.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_contact_view_post_valid(client, settings):
    """Test that a valid form submission sends an email and shows success.

    Args:
        client: Django test client fixture used to perform HTTP requests.
        settings: Django settings fixture used to override email backend.
    """
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    url = reverse("contact:contact")
    data = {
        "name": "Jean Dupont",
        "email": "jean@example.com",
        "subject": "Question sur une location",
        "message": "Bonjour, je voudrais avoir plus d'informations.",
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert "contact/contact.html" in [t.name for t in response.templates]
    assert response.context["success"] is True
    assert len(mail.outbox) == 1
    assert "Question sur une location" in mail.outbox[0].subject


@pytest.mark.django_db
def test_contact_view_post_invalid_email(client):
    """Test that an invalid email re-renders the form with errors.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("contact:contact")
    data = {
        "name": "Jean Dupont",
        "email": "pas-un-email-valide",
        "subject": "Sujet",
        "message": "Message",
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert response.context["success"] is False
    assert len(mail.outbox) == 0


@pytest.mark.django_db
def test_contact_view_post_missing_fields(client):
    """Test that a form with missing fields re-renders with errors.

    Args:
        client: Django test client fixture used to perform HTTP requests.
    """
    url = reverse("contact:contact")
    data = {
        "name": "",
        "email": "",
        "subject": "",
        "message": "",
    }
    response = client.post(url, data)

    assert response.status_code == 200
    assert response.context["success"] is False
    assert len(mail.outbox) == 0


@pytest.mark.django_db
def test_contact_email_content(client, settings):
    """Test that the sent email contains the sender's name and message.

    Args:
        client: Django test client fixture used to perform HTTP requests.
        settings: Django settings fixture used to override email backend.
    """
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    url = reverse("contact:contact")
    data = {
        "name": "Marie Martin",
        "email": "marie@example.com",
        "subject": "Disponibilité",
        "message": "Le bien est-il disponible en août ?",
    }
    client.post(url, data)

    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert "Marie Martin" in email.body
    assert "marie@example.com" in email.body
    assert "Le bien est-il disponible en août ?" in email.body


@pytest.mark.django_db
def test_contact_view_post_resets_form_on_success(client, settings):
    """Test that the form is reset after a successful submission.

    Args:
        client: Django test client fixture used to perform HTTP requests.
        settings: Django settings fixture used to override email backend.
    """
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    url = reverse("contact:contact")
    data = {
        "name": "Paul",
        "email": "paul@example.com",
        "subject": "Info",
        "message": "Merci",
    }
    response = client.post(url, data)

    assert response.context["success"] is True
    assert response.context["form"].initial == {}
