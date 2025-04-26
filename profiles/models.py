"""
Module for the Profile model.

This module defines the Profile model used to store additional user information.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model with user informations.

    :param models: Django's ORM models module.
    :type models: django.db.models
    :return: Instance of Profile representing the user's profile data.
    :rtype: Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the username of the associated User instance.

        :return: The username of the user.
        :rtype: str
        """
        return self.user.username
