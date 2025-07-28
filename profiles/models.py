from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.
    This model extends the default Django User model with additional information
    about the user's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        """
        Returns the username of the associated user.
        Returns:
            str: The username of the user
        """
        return self.user.username
