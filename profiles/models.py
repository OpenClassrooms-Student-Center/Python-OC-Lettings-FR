"""
Database models for the ``profiles`` application.

This module defines the data model used to associate additional
profile information with Django's built-in authentication system.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Store additional information associated with a Django user.

    Each profile is linked to a single ``User`` instance through a
    one-to-one relationship and currently stores the user's favorite city.

    The model extends Django's authentication system without modifying
    the built-in ``User`` model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="new_user")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the username associated with this profile.

        :returns: Username of the related user.
        :rtype: str
        """
        return self.user.username

    class Meta:
        """
        Define metadata associated with the ``Profile`` model.

        The explicit database table name preserves compatibility with the
        original project schema.
        """
        db_table = "profiles_profile"
