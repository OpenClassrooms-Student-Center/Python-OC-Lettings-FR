"""
Application configuration for the lettings app.

This module defines the configuration class used by Django
to register and initialize the lettings application within
the project.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the lettings application.

    This class specifies the application name and allows
    future customization of application-level behavior
    such as signal registration or startup logic.
    """

    name = "lettings"
