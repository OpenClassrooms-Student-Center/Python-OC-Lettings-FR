import pytest

from django.test import Client
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_view():
    """Test the 'letting' view functionality.

    This test verifies that the 'letting' view displays the correct content
    for a given letting object.

    Database setup:
        - Creates an Address instance with specific attributes.
        - Creates a Letting instance associated with the created Address.

    Steps:
        - Makes a GET request to the 'letting' view.
        - Retrieves the response content.
        - Checks if the expected content is present in the response.

    Assertions:
        - Verifies that the response status code is 200 (OK).
        - Verifies that the expected content is present in the response.
    """

    client = Client()
    address = Address.objects.create(id=1, number=30, street='Oratoire', city='Marseille',
                                     state='France', zip_code='13009', country_iso_code='FRA')
    letting = Letting.objects.create(id=1, title="Marseille", address_id=address.id)

    path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<p>Marseille, France 13009</p>"

    assert response.status_code == 200
    assert expected_content in content
