"""
App configuration for the profiles application.

This module defines the ProfilesConfig class, which provides
Django with metadata and configuration for the profiles app.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles app.

    The `name` attribute specifies the full Python path to
    the application, enabling Django to correctly register
    and load the app within the project.
    """
    name = 'profiles'
