# conftest.py
"""
Central test configuration for the Django OC Lettings project.

This module defines reusable pytest fixtures for testing the lettings
application. Fixtures provide pre-created instances of models such as
Address and Letting, which can be injected into unit and integration
tests to ensure consistent and isolated test environments.

Fixtures:
    - address: Creates a sample Address instance.
    - letting: Creates a sample Letting instance linked to an Address.
"""

import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address():
    """
    Fixture that creates a sample Address instance.

    The Address instance represents a physical location with
    predefined fields suitable for testing purposes. The object
    is saved in the test database and is available for injection
    into test functions.

    Returns:
        Address: A saved Address instance with sample data.

    Example usage in a test function:
        def test_address_str(address):
            assert str(address) == "123 Main Street"
    """
    return Address.objects.create(
        number=123,
        street="Main Street",
        city="Los Angeles",
        state="CA",
        zip_code=90001,
        country_iso_code="USA"
    )


@pytest.fixture
def letting(address):
    """
    Fixture that creates a sample Letting instance linked to an Address.

    The Letting instance represents a rental property associated
    with the provided Address fixture. It is saved in the test
    database and can be injected into test functions to test
    model behavior, view responses, and URL routing.

    Args:
        address (Address): A fixture providing an Address instance.

    Returns:
        Letting: A saved Letting instance linked to the provided address.

    Example usage in a test function:
        def test_letting_str(letting):
            assert str(letting) == "Beautiful Apartment"
    """
    return Letting.objects.create(
        title="Beautiful Apartment",
        address=address
    )
