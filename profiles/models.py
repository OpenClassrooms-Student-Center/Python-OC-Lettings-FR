from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Représente un profil client indépendant dans l'application.

    Ce modèle permet de stocker des informations client telles que
    le nom d'utilisateur et la ville favorite.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username
