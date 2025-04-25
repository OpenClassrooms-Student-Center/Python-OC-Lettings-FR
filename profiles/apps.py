"""
Module for the profiles application configuration.
This module contains the configuration class for the profiles app.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    :param AppConfig: Django application's configuration base class.
    :type AppConfig: django.apps.AppConfig
    """
    name = 'profiles'
