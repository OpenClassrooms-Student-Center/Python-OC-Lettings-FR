from django.contrib import admin
from .models import Profile

"""This code registers the Profile model with the Django admin interface."""

admin.site.register(Profile)
