import pytest

from lettings.models import Address, Letting


@pytest.fixture
def get_address():
    """
    Fixture that returns fictive address
    Returns:
        The address object
    """
    return Address.objects.create(
        number=500,
        street="Address test",
        city="City test",
        state="State test",
        zip_code=99999,
        country_iso_code="Country iso code test"
    )


@pytest.fixture
def get_letting(get_address: Address):
    """
    Fixture that returns fictive letting
    Returns:
        The letting object
    """
    return Letting.objects.create(
        title="Test Letting",
        address=get_address
    )
