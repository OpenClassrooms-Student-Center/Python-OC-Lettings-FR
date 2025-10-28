"""
Models for the 'lettings' application, defining the structure for addresses and rental properties.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address for a Letting property.

    Fields:
        number (PositiveIntegerField): The street number (max 9999).
        street (CharField): The street name (max 64 characters).
        city (CharField): The city name (max 64 characters).
        state (CharField): The two-letter state abbreviation (e.g., 'CA').
        zip_code (PositiveIntegerField): The zip code (max 99999).
        country_iso_code (CharField): The three-letter ISO country code (e.g., 'USA').
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Returns a string representation of the Address, showing number and street.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a letting property available for rent.

    Fields:
        title (CharField): The descriptive title of the letting (max 256 characters).
        address (OneToOneField): A one-to-one relationship to the Address model.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the title of the Letting as its string representation.
        """
        return self.title