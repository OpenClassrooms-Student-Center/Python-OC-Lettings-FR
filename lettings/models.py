from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """Model representing an address.

    This model stores information about a physical address,
    including the street number, street name, city, state,
    ZIP code, and country ISO code.

    Attributes:
        number (PositiveIntegerField): The street number.
        street (CharField): The street name.
        city (CharField): The city.
        state (CharField): The state abbreviation (2 characters).
        zip_code (PositiveIntegerField): The ZIP code.
        country_iso_code (CharField): The country ISO code (3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """String representation of the address."""
        return f'{self.number} {self.street}'

    class Meta:
        """Meta options for the Address model."""
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """Model representing a letting (rental property).

    This model stores information about a letting, including
    the title and the associated address.

    Attributes:
        title (CharField): The title of the letting.
        address (OneToOneField): The associated address of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the letting."""
        return self.title
