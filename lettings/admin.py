from django.contrib import admin
from .models import Letting, Address

"""This code registers the Letting and Address models with the Django admin interface."""

admin.site.register(Letting)
admin.site.register(Address)
