from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address with specific fields for number, street, city, state, zip code,
    and country ISO code.

    Attributes:
        number (PositiveIntegerField): The house/building number, validated to be a max of 9999.
        street (CharField): The name of the street, with a maximum length of 64 characters.
        city (CharField): The name of the city, with a maximum length of 64 characters.
        state (CharField): The two-character state code, validated to have a minimum length of 2.
        zip_code (PositiveIntegerField): The postal code, validated to be a maximum of 99999.
        country_iso_code (CharField): The ISO code for the country, have a min length of 3.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a string representation of the Address instance, typically used in the Django admin
        interface.

        Returns:
            str: A string combining the number and street.
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Metadata options for the Address model.

        Attributes:
            verbose_name_plural (str): The plural name for the model used in the admin interface.
        """
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a letting which includes a title and is associated with a specific address.

    Attributes:
        title (CharField): The title of the letting, with a maximum length of 256 characters.
        address (OneToOneField): A one-to-one relationship with an Address, where the address is
                                 deleted if the letting is deleted.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the Letting instance, typically used in the Django
        admin interface.

        Returns:
            str: The title of the letting.
        """
        return self.title
