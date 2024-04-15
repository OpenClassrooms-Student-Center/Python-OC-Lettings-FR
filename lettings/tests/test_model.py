import pytest
from ..models import Address, Letting
from django.test import TestCase


class TestAddress:

    #  Creating a valid Address object with all fields filled in correctly
    def test_create_valid_address(self):
        # Arrange
        number = 123
        street = "Main St"
        city = "New York"
        state = "NY"
        zip_code = 12345
        country_iso_code = "USA"

        # Act
        address = Address(number=number,
                          street=street,
                          city=city,
                          state=state,
                          zip_code=zip_code,
                          country_iso_code=country_iso_code
                          )

        # Assert
        assert address.number == number
        assert address.street == street
        assert address.city == city
        assert address.state == state
        assert address.zip_code == zip_code
        assert address.country_iso_code == country_iso_code

    #  Updating an existing Address object with valid data
    def test_update_address(self):
        # Arrange
        number = 123
        street = "Main St"
        city = "New York"
        state = "NY"
        zip_code = 12345
        country_iso_code = "USA"

        address = Address(number=number,
                          street=street,
                          city=city,
                          state=state,
                          zip_code=zip_code,
                          country_iso_code=country_iso_code
                          )

        new_number = 456
        new_street = "Elm St"
        new_city = "Los Angeles"
        new_state = "CA"
        new_zip_code = 67890
        new_country_iso_code = "USA"

        # Act
        address.number = new_number
        address.street = new_street
        address.city = new_city
        address.state = new_state
        address.zip_code = new_zip_code
        address.country_iso_code = new_country_iso_code

        # Assert
        assert address.number == new_number
        assert address.street == new_street
        assert address.city == new_city
        assert address.state == new_state
        assert address.zip_code == new_zip_code
        assert address.country_iso_code == new_country_iso_code

    #  Retrieving the string representation of an Address object
    def test_string_representation(self):
        # Arrange
        number = 123
        street = "Main St"
        city = "New York"
        state = "NY"
        zip_code = 12345
        country_iso_code = "USA"

        address = Address(number=number,
                          street=street,
                          city=city,
                          state=state,
                          zip_code=zip_code,
                          country_iso_code=country_iso_code
                          )

        expected_string = f'{number} {street}'

        # Act
        result = str(address)

        # Assert
        assert result == expected_string

    #  Creating an Address object with the maximum allowed values for all fields
    def test_create_address_with_maximum_values(self):
        # Arrange
        number = 9999
        street = "A" * 64
        city = "A" * 64
        state = "AA"
        zip_code = 99999
        country_iso_code = "AAA"

        # Act
        address = Address(number=number,
                          street=street,
                          city=city,
                          state=state,
                          zip_code=zip_code,
                          country_iso_code=country_iso_code
                          )

        # Assert
        assert address.number == number
        assert address.street == street
        assert address.city == city
        assert address.state == state
        assert address.zip_code == zip_code
        assert address.country_iso_code == country_iso_code

    #  Creating an Address object with the minimum allowed values for all fields
    def test_create_address_with_minimum_values(self):
        # Arrange
        number = 0
        street = ""
        city = ""
        state = "A"
        zip_code = 0
        country_iso_code = "AA"

        # Act
        address = Address(number=number,
                          street=street,
                          city=city,
                          state=state,
                          zip_code=zip_code,
                          country_iso_code=country_iso_code
                          )

        # Assert
        assert address.number == number
        assert address.street == street
        assert address.city == city
        assert address.state == state
        assert address.zip_code == zip_code
        assert address.country_iso_code == country_iso_code

    #  Creating an Address object with a street name that is the maximum allowed length
    def test_create_address_with_maximum_street_length(self):
        # Arrange
        number = 123
        street = "A" * 64
        city = "New York"
        state = "NY"
        zip_code = 12345
        country_iso_code = "USA"

        # Act
        address = Address(number=number,
                          street=street,
                          city=city,
                          state=state,
                          zip_code=zip_code,
                          country_iso_code=country_iso_code
                          )

        # Assert
        assert address.number == number
        assert address.street == street
        assert address.city == city
        assert address.state == state
        assert address.zip_code == zip_code
        assert address.country_iso_code == country_iso_code


class TestLetting(TestCase):

    #  Letting object can be created with a valid title and address
    def test_letting_creation_with_valid_title_and_address(self):
        # Arrange
        title = "Valid Title"
        address = Address(number=123, street="Valid Street", city="Valid City", state="CA", zip_code=12345,
                          country_iso_code="USA")

        # Act
        letting = Letting(title=title, address=address)

        # Assert
        assert letting.title == title
        assert letting.address == address

    def test_letting_save_to_database(self):
        # Arrange
        title = "Valid Title"
        address = Address.objects.create(number=123, street="Valid Street", city="Valid City", state="CA",
                                         zip_code=12345,
                                         country_iso_code="USA")
        letting = Letting.objects.create(title=title, address=address)

        # Act & Assert
        assert Letting.objects.filter(title=title).exists()

    def test_letting_retrieve_from_database(self):
        # Arrange
        title = "Valid Title"
        address = Address.objects.create(number=123, street="Valid Street", city="Valid City", state="CA",
                                         zip_code=12345,
                                         country_iso_code="USA")
        letting = Letting.objects.create(title=title, address=address)

        # Act
        retrieved_letting = Letting.objects.get(title=title)

        # Assert
        assert retrieved_letting == letting

