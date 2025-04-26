"""
Module for lettings models.

This module defines the Address and Letting models used to represent lettings data.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.

    This model stores address details such as number, street,
    city, state, zip code, and country ISO code.

    :param models: Django's ORM models module.
    :type models: django.db.models
    :return: An instance of Address representing a physical address.
    :rtype: Address
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Return a string representation of the address.

        :return: A string combining the number and street.
        :rtype: str
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        This class defines the verbose name and plural form for the Address model.
        """
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a letting.

    This model stores information about a letting, including its title and the associated address.

    :param models: Django's ORM models module.
    :type models: django.db.models
    :return: An instance of Letting representing a letting record.
    :rtype: Letting
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the title of the letting.

        :return: The title of the letting.
        :rtype: str
        """
        return self.title
