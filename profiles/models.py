"""
Models module for profiles app
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Models class for profiles app
    Attributes:
        user (User): user
        favorite_city (str): The favorite city of the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        """
        String method for profile model
        Returns:
        The user name of the profile
        """
        return self.user.username
