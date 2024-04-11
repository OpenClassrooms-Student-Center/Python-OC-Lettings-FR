from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model representing a user profile.

    This model stores additional information about a user,
    such as their favorite city.

    Attributes:
        user (OneToOneField): The associated user.
        favorite_city (CharField): The user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """String representation of the user profile."""
        return self.user.username
