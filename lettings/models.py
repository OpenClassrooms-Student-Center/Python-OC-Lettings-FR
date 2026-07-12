"""
Database models for the ``lettings`` application.

This module defines the data models used to represent rental properties
and their associated addresses.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represent the physical location of a rental property.

    This model stores the address associated with a letting and
    enforces basic validation rules on its fields to ensure data
    consistency.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self) -> str:
        """
        Return a readable representation of the address.

        :returns: Street number followed by the street name.
        :rtype: str
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        Define metadata associated with the ``Address`` model.

        The explicit database table name preserves compatibility with the
        original project schema.
        """

        db_table = "lettings_address"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represent a rental property available through the application.

    Each letting is associated with a unique ``Address`` instance,
    allowing the application to separate property information from
    location data.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the title of the letting.

        :returns: Letting title.
        :rtype: str
        """
        return self.title

    class Meta:
        """
        Define metadata associated with the ``Letting`` model.

        The explicit database table name preserves compatibility with the
        original project schema.
        """

        db_table = "lettings_letting"
