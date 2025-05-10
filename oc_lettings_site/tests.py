"""
Unit tests for the oc_lettings_site app.

This module contains test cases for views and urls of the main application.
"""

from django.test import TestCase
from django.urls import reverse


class TestOCLettingsSite(TestCase):
    """Test class for oc_lettings_site app."""

    def test_index_view(self):
        """Test the main index view."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('Welcome', str(response.content))

    def test_error_404_view(self):
        """Test the 404 error view."""
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_error_500_view(self):
        """Test the 500 error view."""
        with self.assertRaises(Exception):
            self.client.get(reverse('error_500'))
