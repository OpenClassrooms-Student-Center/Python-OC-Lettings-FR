import pytest

from django.urls import reverse, resolve
from lettings.models import Address


@pytest.mark.django_db
def test_lettings_url():
    """Test the generation and resolution of the URL for the 'letting' view.

    This test ensures that the URL for the 'letting' view is generated correctly
    and that it resolves to the expected view function.

    Database setup:
       - Creates an Address instance with specific attributes.

    Assertions:
       - Verifies that the generated URL matches '/lettings/1/'.
       - Verifies that the resolved view name is 'lettings:letting'.
    """

    Address.objects.create(id=1, number=30, street='Oratoire', city='Marseille',
                           state='France', zip_code='13009', country_iso_code='FRA')

    path = reverse('lettings:letting', kwargs={'letting_id': 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == 'lettings:letting'
