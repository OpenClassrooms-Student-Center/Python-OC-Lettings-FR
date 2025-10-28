"""
Models for the 'profiles' application, defining extended user information 
via the Profile model linked to Django's built-in User model.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents additional, specific profile information for a user.

    Fields:
        user (OneToOneField): A one-to-one link to the standard Django User model.
        favorite_city (CharField): The user's favorite city (max 64 characters, optional).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns the username of the linked user as the string representation.
        """
        return self.user.username