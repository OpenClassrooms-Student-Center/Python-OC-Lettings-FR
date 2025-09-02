from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Représente une adresse postale complète.

    Contient les informations nécessaires pour identifier un lieu :
    numéro, rue, ville, état, code postal du pays.
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
        Retourne une version lisible de l’adresse (numéro et rue).
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Représente une location disponible.

    Contient un titre descriptif et une relation
    vers une adresse unique associée à cette location.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lettings"

    def __str__(self):
        """
        Retourne le titre de la location.
        """
        return self.title
