"""Models for the lettings application.

This module defines the data structures used to represent
postal addresses and rental properties (lettings) in the system.
"""

from django.db import models
from cloudinary.models import CloudinaryField


class Address(models.Model):
    """Represents a postal address.

    Attributes:
        number: The street number as a positive integer.
        street: The street name.
        city: The city name.
        state: The state, region or province name.
        zip_code: The postal or ZIP code.
        country_iso_code: The ISO 3166-1 alpha-3 country code.
    """

    number = models.PositiveIntegerField()
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    country_iso_code = models.CharField(max_length=3)

    def __str__(self):
        """Return a human-readable representation of the address.

        Returns:
            A string containing the street number and street name.
        """
        # Les tests attendent "10 Str", donc seulement number + street
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Represents a rental property.

    A letting is defined by a title and a one-to-one relationship
    with an Address instance.

    Attributes:
        title: The public title of the letting.
        address: The associated Address instance.
    """
    reference = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        help_text="Référence unique du logement (ex: LOC-2026-001)"
    )
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    image = CloudinaryField("image", blank=True, null=True)
    description = models.TextField(blank=True, default="")
    price_per_night = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    rooms = models.PositiveIntegerField(null=True, blank=True)
    area = models.PositiveIntegerField(null=True, blank=True, help_text="Surface en m²")

    class Meta:
        """Django model metadata for Letting."""

        verbose_name_plural = "Addresses"

    def __str__(self):
        """Return the letting title as its string representation.

        Returns:
            The title of the letting.
        """
        return self.title

    def save(self, *args, **kwargs):
        if not self.reference:
            super().save(*args, **kwargs)
            self.reference = f"LOC-{self.pk:04d}"
            Letting.objects.filter(pk=self.pk).update(reference=self.reference)
        else:
            super().save(*args, **kwargs)

    @property                          # ← à l'intérieur de Letting
    def image_url(self):
        """Retourne l'URL de l'image principale ou None."""
        try:
            return self.image.url if self.image else None
        except Exception:
            return None

    def all_images(self):
        """Retourne toutes les URLs d'images : principale + galerie, max 10."""
        images = []
        if self.image:
            images.append(self.image.url)
        for img in self.gallery_images.all()[:9]:
            images.append(img.image.url)
        return images[:10]


class LettingImage(models.Model):
    """Image supplémentaire liée à une location."""

    letting = models.ForeignKey(
        Letting,
        on_delete=models.CASCADE,
        related_name="gallery_images"
    )
    image = CloudinaryField("image")
    order = models.PositiveIntegerField(default=0, help_text="Ordre d'affichage")

    class Meta:
        ordering = ["order"]
        verbose_name = "Image galerie"
        verbose_name_plural = "Images galerie"

    def __str__(self):
        return f"Image {self.order} — {self.letting.title}"
