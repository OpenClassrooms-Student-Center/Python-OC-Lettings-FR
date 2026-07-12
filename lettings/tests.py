"""
Unit tests for the lettings.models module.

This file contains tests for the Address and Letting models,
ensuring that model fields, string representations, and
basic validations work correctly.

Fixtures:
    - address: Pre-created Address instance for tests.
"""

import pytest
from django.urls import reverse, resolve
from lettings import views


@pytest.mark.django_db
def test_address_str(address):
    """
    Test the string representation of the Address model.

    The __str__ method should return a formatted string combining
    the street number and the street name.

    Args:
        address (Address): Fixture providing a sample Address instance.
    """
    assert str(address) == "123 Main Street"


@pytest.mark.django_db
def test_address_fields(address):
    """
    Test that the Address fields are correctly set from the fixture.

    Args:
        address (Address): Fixture providing a sample Address instance.
    """
    assert address.number == 123
    assert address.street == "Main Street"
    assert address.city == "Los Angeles"
    assert address.state == "CA"
    assert address.zip_code == 90001
    assert address.country_iso_code == "USA"


"""
Unit tests for the Letting model in lettings.models.

This file contains tests for the Address and Letting models,
ensuring that model fields, string representations, and
one-to-one relationships work correctly.
"""


@pytest.mark.django_db
def test_letting_str(letting):
    """
    Test the string representation of the Letting model.

    The __str__ method should return the title of the letting.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    assert str(letting) == "Beautiful Apartment"


@pytest.mark.django_db
def test_letting_fields(letting, address):
    """
    Test that the Letting fields are correctly set and linked to Address.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
        address (Address): Fixture providing a sample Address instance.
    """
    assert letting.title == "Beautiful Apartment"
    # Check the one-to-one relationship
    assert letting.address == address
    # Confirm related data
    assert letting.address.street == "Main Street"
    assert letting.address.city == "Los Angeles"


"""
URL tests for the lettings application.

This module verifies that URL patterns defined in lettings.urls
correctly resolve to their associated view functions and that
named routes generate the expected paths.

The following aspects are tested:
- URL reversing using Django's reverse function
- URL resolution using Django's resolve function
- HTTP response status codes for defined routes
"""


@pytest.mark.django_db
def test_lettings_index_url_reverse():
    """
    Test that the lettings index URL is correctly reversed.

    Ensures that the named route 'lettings:lettings_index'
    generates the expected URL path.
    """
    url = reverse("lettings:lettings_index")
    assert url == "/lettings/"


@pytest.mark.django_db
def test_letting_detail_url_reverse(letting):
    """
    Test that the letting detail URL is correctly reversed
    with a valid letting ID.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    url = reverse("lettings:letting", args=[letting.id])
    assert url == f"/lettings/{letting.id}/"


@pytest.mark.django_db
def test_lettings_index_url_resolves():
    """
    Test that the lettings index URL resolves
    to the correct view function.
    """
    resolver = resolve("/lettings/")
    assert resolver.func == views.lettings_index


@pytest.mark.django_db
def test_letting_detail_url_resolves(letting):
    """
    Test that the letting detail URL resolves
    to the correct view function.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    resolver = resolve(f"/lettings/{letting.id}/")
    assert resolver.func == views.letting


@pytest.mark.django_db
def test_lettings_index_http_response(client):
    """
    Integration test ensuring that the lettings index
    URL returns an HTTP 200 response.
    """
    response = client.get(reverse("lettings:lettings_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_http_response(client, letting):
    """
    Integration test ensuring that the letting detail
    URL returns an HTTP 200 response for a valid ID.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert response.status_code == 200


"""
View tests for the lettings application.

This module verifies that view functions defined in lettings.views
correctly render templates, return expected HTTP responses,
and provide appropriate context data.

The following views are tested:
- lettings_index
- letting
"""


@pytest.mark.django_db
def test_lettings_index_view_status_code(client):
    """
    Test that the lettings_index view returns HTTP 200.
    """
    response = client.get(reverse("lettings:lettings_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_index_view_template(client):
    """
    Test that the correct template is used
    for the lettings_index view.
    """
    response = client.get(reverse("lettings:lettings_index"))
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_lettings_index_context(client, letting):
    """
    Test that the lettings_index view provides
    the correct context data.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    response = client.get(reverse("lettings:lettings_index"))

    assert "lettings_list" in response.context
    assert letting in response.context["lettings_list"]


@pytest.mark.django_db
def test_letting_detail_view_status_code(client, letting):
    """
    Test that the letting detail view returns HTTP 200
    for a valid letting ID.
    """
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_view_template(client, letting):
    """
    Test that the correct template is used
    for the letting detail view.
    """
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert "lettings/letting.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_letting_detail_context(client, letting):
    """
    Test that the letting detail view provides
    the correct context variables.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    response = client.get(reverse("lettings:letting", args=[letting.id]))

    assert response.context["title"] == letting.title
    assert response.context["address"] == letting.address


@pytest.mark.django_db
def test_letting_detail_invalid_id_returns_404(client):
    """
    Ensure that requesting a non-existing letting returns HTTP 404.

    The view now uses get_object_or_404, which should return a
    404 response instead of raising an exception.
    """
    response = client.get(reverse("lettings:letting", args=[9999]))

    assert response.status_code == 404


"""
Integration tests for the `lettings` Django application.

These tests validate the behavior of the application by exercising
the full request/response cycle of the Django stack:

    URL routing → View execution → Database access → Template rendering → HTTP response

Unlike unit tests that focus on isolated components (models, views, or URLs),
integration tests ensure that multiple layers of the application work together
correctly when accessed through real HTTP requests.

The following scenarios are covered:

Happy paths:
    - Accessing the lettings index page successfully
    - Displaying existing lettings in the index page
    - Navigating to the detail page of a specific letting
    - Displaying letting address information correctly

Edge cases:
    - Rendering the index page when no lettings exist

Sad paths (TDD approach):
    - Requesting a letting that does not exist should return HTTP 404

Some tests intentionally document expected future behavior such as
proper 404 error handling. These tests may initially fail until the
application implements the appropriate error management.

This approach follows Test-Driven Development (TDD) principles.
"""


@pytest.mark.django_db
def test_lettings_index_page_accessible(client):
    """
    Verify that the lettings index page is accessible via HTTP.

    This test ensures that the URL associated with the lettings index
    view is correctly configured and returns a valid HTTP response.

    The test validates that:
        - The URL can be resolved using Django's reverse function
        - The HTTP response status code is 200 (OK)
        - The correct template is used to render the page

    This confirms that URL routing, view execution, and template
    rendering work correctly together.
    """
    url = reverse("lettings:lettings_index")

    response = client.get(url)

    assert response.status_code == 200
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_lettings_index_displays_existing_lettings(client, letting):
    """
    Verify that existing lettings are displayed on the index page.

    This test creates a Letting instance using a fixture and ensures
    that the index page correctly retrieves and renders the letting
    information.

    The test validates that:
        - The letting instance is retrieved from the database
        - The letting title appears in the rendered HTML response

    This confirms that the view properly interacts with the database
    and passes the expected context data to the template.
    """
    url = reverse("lettings:lettings_index")

    response = client.get(url)

    content = response.content.decode()

    assert letting.title in content


@pytest.mark.django_db
def test_lettings_index_handles_empty_dataset(client):
    """
    Verify the behavior of the index page when no lettings exist.

    When the database contains no Letting instances, the template
    should display a fallback message informing the user that
    no lettings are available.

    The test validates that:
        - The page still renders successfully
        - The appropriate message appears in the response

    This ensures the application handles empty datasets gracefully.
    """
    url = reverse("lettings:lettings_index")

    response = client.get(url)

    content = response.content.decode()

    assert response.status_code == 200
    assert "No lettings are available." in content


@pytest.mark.django_db
def test_letting_detail_page_accessible(client, letting):
    """
    Verify that a letting detail page can be accessed successfully.

    This test ensures that a valid letting ID correctly resolves
    to the letting detail view and that the page renders without errors.

    The test validates that:
        - The correct URL is generated using reverse()
        - The view retrieves the letting from the database
        - The correct template is used to render the page
        - The HTTP response status is 200 (OK)

    This confirms the correct integration of URL routing,
    database access, and template rendering.
    """
    url = reverse("lettings:letting", args=[letting.id])

    response = client.get(url)

    assert response.status_code == 200
    assert "lettings/letting.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_letting_detail_displays_address_information(client, letting):
    """
    Verify that the letting detail page displays address information.

    This test ensures that the address fields associated with the
    letting instance are correctly passed to the template and rendered
    in the final HTML output.

    The test checks that the response contains:
        - the letting title
        - the street name
        - the city name

    This confirms that the relationship between Letting and Address
    models is correctly handled and displayed by the view and template.
    """
    url = reverse("lettings:letting", args=[letting.id])

    response = client.get(url)

    content = response.content.decode()

    assert letting.title in content
    assert letting.address.street in content
    assert letting.address.city in content


@pytest.mark.django_db
def test_letting_detail_returns_404_for_unknown_letting(client):
    """
    Verify that requesting a non-existent letting returns HTTP 404.

    This test represents the expected behavior for the application
    when a user attempts to access a letting that does not exist
    in the database.

    According to REST and Django best practices, the application
    should return an HTTP 404 (Not Found) response instead of
    raising an unhandled exception.

    This test follows a Test-Driven Development (TDD) approach:
        - It defines the expected behavior first
        - The test may initially fail if the view does not yet
          implement proper 404 handling

    The test will pass once the view uses Django's `get_object_or_404`
    helper or equivalent error handling.
    """
    url = reverse("lettings:letting", args=[9999])

    response = client.get(url)

    assert response.status_code == 404
    assert "Sorry, the page you are looking for does not exist." in response.content.decode()


"""
Integration tests for the main Django project application `oc_lettings_site`.

These tests validate the behavior of the project's root-level views and
their integration with the rest of the Django application stack.

Unlike unit tests that verify isolated components, these tests exercise
the full request-response lifecycle:

    URL routing → View execution → Template rendering → HTTP response

The main goal of these tests is to ensure that the project’s entry point
(the home page) behaves correctly and provides valid navigation to the
different Django applications included in the project.

The following scenarios are covered:

Happy paths:
    - Accessing the home page successfully
    - Rendering the correct template for the home page
    - Displaying navigation links to the lettings and profiles sections

Integration validation:
    - Ensuring the navigation links resolve to valid URLs
    - Verifying that cross-application routing is correctly configured

Sad paths (TDD preparation):
    - Documenting expected 404 behavior for unknown routes

Some tests may initially fail if global error handling (404 / 500 pages)
is not yet implemented. This follows a Test-Driven Development (TDD)
approach where expected behaviors are specified before implementation.
"""


@pytest.mark.django_db
def test_homepage_accessible(client):
    """
    Verify that the project home page is accessible.

    This test ensures that the root URL of the application resolves
    correctly to the index view and returns a valid HTTP response.

    The test validates that:
        - Django can resolve the URL using reverse()
        - The HTTP response status code is 200 (OK)

    This confirms that the project's main entry point is correctly
    configured and accessible to users.
    """
    url = reverse("index")

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_homepage_uses_correct_template(client):
    """
    Verify that the home page uses the correct template.

    The index view should render the 'index.html' template. This test
    ensures that the template rendering layer is correctly connected
    to the view.

    This confirms the integration between:
        - URL routing
        - view execution
        - template rendering
    """
    url = reverse("index")

    response = client.get(url)

    templates = [t.name for t in response.templates]

    assert "index.html" in templates


@pytest.mark.django_db
def test_homepage_displays_navigation_links(client):
    """
    Verify that the home page displays navigation links to the main
    sections of the application.

    The index page should contain links allowing users to navigate
    to both the lettings and profiles sections.

    This test validates that:
        - the link to the lettings index page is present
        - the link to the profiles index page is present

    This confirms that the template correctly integrates URL
    resolution using Django's `{% url %}` template tag.
    """
    url = reverse("index")

    response = client.get(url)

    content = response.content.decode()

    lettings_url = reverse("lettings:lettings_index")
    profiles_url = reverse("profiles:profiles_index")

    assert lettings_url in content
    assert profiles_url in content


@pytest.mark.django_db
def test_navigation_to_lettings_page(client):
    """
    Verify that the lettings section is reachable from the project.

    This test ensures that the root URL configuration correctly
    includes the URL patterns defined in the `lettings` application.

    The test validates that:
        - the lettings index URL resolves correctly
        - accessing the page returns HTTP 200

    This confirms that cross-application URL inclusion works as expected.
    """
    url = reverse("lettings:lettings_index")

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_navigation_to_profiles_page(client):
    """
    Verify that the profiles section is reachable from the project.

    This test ensures that the root URL configuration correctly
    includes the URL patterns defined in the `profiles` application.

    The test validates that:
        - the profiles index URL resolves correctly
        - accessing the page returns HTTP 200

    This confirms that cross-application routing is properly configured.
    """
    url = reverse("profiles:profiles_index")

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_unknown_url_returns_404(client):
    """
    Verify that requesting an unknown URL returns HTTP 404.

    According to standard web application behavior, when a user
    requests a route that does not exist, the server should return
    a 404 (Not Found) response.

    This test documents the expected behavior for invalid routes.

    It also prepares the test suite for future implementation of
    custom 404 error pages within the project.

    This test follows a Test-Driven Development (TDD) approach and
    may evolve once dedicated error handlers are implemented.
    """
    response = client.get("/this-page-does-not-exist/")

    assert response.status_code == 404
    assert "Sorry, the page you are looking for does not exist." in response.content.decode()
