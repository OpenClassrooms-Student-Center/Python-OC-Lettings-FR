"""
Models module for lettings app
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Address model for Lettings
    Attributes:
        number (int): Letting number
        street (str): Street address
        city (str): City address
        state (str): State address
        zip_code (int): Zip code
        country_iso_code (int): Country code
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        Meta class for Lettings to specify verbose names
        """
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self) -> str:
        """
        string method for Lettings
        Returns:
        A f-string with number and street address
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Letting model for Lettings
    Attributes:
        title (str): Letting title
        address (Address): Letting address
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        String method for Lettings
        Returns:
        A f-string with letting title
        """
        return self.title
