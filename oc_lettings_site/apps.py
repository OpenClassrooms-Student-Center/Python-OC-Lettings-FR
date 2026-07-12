"""
Application configuration for the oc_lettings_site project.

This module defines the configuration class used by Django
to initialize and register the main project application.

Although minimal, this configuration class serves as the
entry point for application-level customization, such as
signal registration or startup logic.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration class for the oc_lettings_site application.

    This class declares the application name and provides a
    foundation for future project-wide initialization behavior.
    """

    name = "oc_lettings_site"
