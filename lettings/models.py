from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """ Manage address informations

    Args:
        models (_type_): _description_

    Returns:
        Address: a class instance with adress data
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """ The address main informations

        Returns:
            str: number and street
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """ manage informations about letting

    Args:
        models (_type_): _description_

    Returns:
        Letting: give title and adress data
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """ The title of letting

        Returns:
            str: title
        """
        return self.title
