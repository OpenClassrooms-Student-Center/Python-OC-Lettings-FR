from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a profile with a user,
    ( with a related name and a related query name )
    and a favorite city.
    """
    user = models.OneToOneField(User,

                                on_delete=models.CASCADE,
                                related_name='profile_user',
                                related_query_name='profile_user_query'
                                )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
