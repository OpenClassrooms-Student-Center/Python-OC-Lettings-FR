"""
Admin configuration for the lettings application.

This module registers the Letting and Address models
with the Django admin interface, allowing administrators
to manage lettings and related address data through
the built-in Django admin site.
"""

from django.contrib import admin

from .models import Letting
from .models import Address


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Letting model.

    This class enables the management of Letting instances
    within the Django admin interface.
    """

    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Address model.

    This class enables the management of Address instances
    within the Django admin interface.
    """

    pass
