"""
Module for the lettings application configuration.

This module defines the configuration class for the lettings app.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the lettings application.
    This class is used to set up the application and its settings.
    It inherits from Django's AppConfig base class.

    :param AppConfig: Django's application configuration base class.
    :type AppConfig: django.apps.AppConfig
    """
    name = 'lettings'
