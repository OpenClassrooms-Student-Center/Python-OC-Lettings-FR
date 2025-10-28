"""
Admin configuration for the 'lettings' application.

Registers the Letting and Address models for management in the Django Admin interface.
"""
from django.contrib import admin
from .models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)