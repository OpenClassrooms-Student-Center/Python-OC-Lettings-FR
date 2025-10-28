"""
Admin configuration for the 'profiles' application.

Registers the Profile model for management in the Django Admin interface.
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)