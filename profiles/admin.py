"""
Admin registration module for profiles app
"""
from django.contrib import admin

from profiles.models import Profile


admin.site.register(Profile)
