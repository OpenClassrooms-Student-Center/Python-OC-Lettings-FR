from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile that extends the built-in User model with additional information.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the built-in User model,
                              where the profile is deleted if the user is deleted.
        favorite_city (CharField): An optional field to store the user's favorite city,
                                   with a maximum length of 64 characters.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the Profile instance, typically used in the Django
        admin interface.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
