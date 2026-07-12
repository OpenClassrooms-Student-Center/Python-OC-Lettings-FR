"""
URL tests for the main Django project (oc_lettings_site).

This module verifies that the root URL configuration correctly
routes requests to the expected views or included URL modules.

The following aspects are tested:
- URL reversing for the home page
- URL resolution for the home page
- HTTP response for the home page
- Accessibility of included URL patterns (lettings, profiles, admin)
"""

import pytest
from django.urls import reverse, resolve
from oc_lettings_site import views

from django.test import RequestFactory
from django.core.handlers.exception import response_for_exception


@pytest.mark.django_db
def test_index_url_reverse():
    """
    Test that the home page URL is correctly reversed.

    Ensures that the named route 'index'
    generates the expected root path.
    """
    url = reverse("index")
    assert url == "/"


@pytest.mark.django_db
def test_index_url_resolves():
    """
    Test that the home page URL resolves
    to the correct view function.
    """
    resolver = resolve("/")
    assert resolver.func == views.index


@pytest.mark.django_db
def test_index_http_response(client):
    """
    Integration test ensuring that the home page
    returns an HTTP 200 response.
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_url_accessible(client):
    """
    Test that the lettings URL prefix is accessible
    through the project-level URL configuration.
    """
    response = client.get("/lettings/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_url_accessible(client):
    """
    Test that the profiles URL prefix is accessible
    through the project-level URL configuration.
    """
    response = client.get("/profiles/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_url_accessible(client):
    """
    Test that the Django admin interface
    is accessible through the project URL configuration.

    Note:
        The admin page may redirect to the login page
        if the user is not authenticated.
    """
    response = client.get("/admin/")
    assert response.status_code in (200, 302)


"""
View tests for the main Django project (oc_lettings_site).

This module verifies that the project-level views return
correct HTTP responses and render the expected templates.

The following view is tested:
- index
"""


@pytest.mark.django_db
def test_index_view_status_code(client):
    """
    Test that the index view returns HTTP 200.
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_view_template(client):
    """
    Test that the index view renders the correct template.
    """
    response = client.get(reverse("index"))
    assert "index.html" in [t.name for t in response.templates]


def test_500_handler_unit():
    factory = RequestFactory()
    request = factory.get("/")

    try:
        raise Exception("forced")
    except Exception as e:
        response = response_for_exception(request, e)

    assert response.status_code == 500
    assert "Something went wrong on our side" in response.content.decode()
