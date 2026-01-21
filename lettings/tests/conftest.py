import pytest
from lettings.models import Address, Letting


@pytest.fixture
def sample_address():
    return Address.objects.create(
        number=123,
        street="Main St",
        city="Springfield",
        state="IL",
        zip_code=62704,
        country_iso_code="USA"
    )


@pytest.fixture
def sample_letting(sample_address):
    return Letting.objects.create(
        title="Cozy Cottage",
        address=sample_address
    )


@pytest.fixture
def multiple_lettings():
    """
    Create 3 different lettings with their addresses for testing.
    Returns a list of Letting objects.
    """
    return [
        Letting.objects.create(
            title=f"Cozy Cottage {i}",
            address=Address.objects.create(
                number=123 + i,
                street="Main St",
                city="Springfield",
                state="IL",
                zip_code=62704 + i,
                country_iso_code="USA"
            )
        ) for i in range(1, 4)
    ]
