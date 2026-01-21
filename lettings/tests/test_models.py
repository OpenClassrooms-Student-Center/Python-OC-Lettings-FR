import pytest


class TestAddressModel:

    @pytest.mark.django_db
    def test_address_str(self, sample_address):
        """
        Test the string representation of the Address model.
        """
        assert str(sample_address) == "123 Main St"


class TestLettingModel:

    @pytest.mark.django_db
    def test_letting_str(self, sample_letting):
        """
        Test the string representation of the Letting model.
        """
        assert str(sample_letting) == "Cozy Cottage"
