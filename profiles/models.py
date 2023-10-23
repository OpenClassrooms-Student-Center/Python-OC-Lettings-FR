from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ manage profile informations

    Args:
        models (_type_): _description_

    Returns:
        Profile: Give standard user informations and favorite_city
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """ Give user username

        Returns:
            str: username
        """
        return self.user.username
