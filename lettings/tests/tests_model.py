"""
Tests module for lettings app models
"""
import pytest

from lettings.models import Letting, Address


class TestLettingsModel:
    @pytest.mark.django_db
    def test_lettings_address_model_ok(self, get_address: Address):
        """
        Method to test if an address object is created correctly
        Args:
            get_address (Adress): Address object
        """
        expected = f"{get_address.number} {get_address.street}"

        assert str(get_address) == expected

    @pytest.mark.django_db
    def test_lettings_letting_model_ok(self, get_letting: Letting):
        """
        Method to test if a letting object is created correctly
        Args:
            get_letting (Letting): Letting object
        """
        expected = f"{get_letting.title}"

        assert str(get_letting) == expected
