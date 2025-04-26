"""
Admin configuration for profiles app.

This module registers the Profile model with the Django admin interface
to allow management of user profiles through the administration panel.
"""

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
