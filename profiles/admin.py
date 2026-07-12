"""
Admin configuration for the profiles application.

This module registers the Profile model with the Django admin interface,
allowing administrators to manage user profile data through
the built-in Django admin site.
"""

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.

    This class enables the management of Profile instances
    within the Django admin interface.
    """

    pass
