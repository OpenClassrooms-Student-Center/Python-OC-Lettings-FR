"""
Admin configuration for lettings app.

This module registers the Letting and Address models with the Django admin interface
to allow management of lettings and addresses through the administration panel.
"""

from django.contrib import admin
from .models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)
