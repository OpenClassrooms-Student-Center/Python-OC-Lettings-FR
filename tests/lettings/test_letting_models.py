from django.test import TestCase
from lettings.models import Address, Letting


class LettingsModelsTestCase(TestCase):

    def test_address_model(self):

        address = Address.objects.create(
            number=100, street="My street", city="My city",
            state="My state", zip_code=10000,
            country_iso_code="USA"
        )
        expected_value = "100 My street"
        assert str(address) == expected_value

    def test_letting_model(self):
        address = Address.objects.create(
            number=100, street="My street", city="My city",
            state="My state", zip_code=10000,
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title="My letting",
            address=address
        )
        expected_value = "My letting"
        assert str(letting) == expected_value
