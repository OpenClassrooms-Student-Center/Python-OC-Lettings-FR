"""
Unit tests for the lettings app.

This module contains test cases for models, views and urls of the lettings application.
"""

from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class TestLettings(TestCase):
    """Test class for lettings app."""

    def setUp(self):
        """Set up test data."""
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST"
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_address_str_method(self):
        """Test the string representation of Address model."""
        assert str(self.address) == "123 Test Street"

    def test_letting_str_method(self):
        """Test the string representation of Letting model."""
        assert str(self.letting) == "Test Letting"

    def test_lettings_index_view(self):
        """Test the index view of lettings app."""
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Lettings", str(response.content))
        self.assertEqual(response.templates[0].name, 'lettings/index.html')

    def test_letting_detail_view(self):
        """Test the detail view of a letting."""
        url = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.letting.title, str(response.content))
        self.assertEqual(response.templates[0].name, 'lettings/letting.html')

    def test_letting_detail_view_404(self):
        """Test the detail view with invalid letting id."""
        url = reverse('lettings:letting', kwargs={'letting_id': 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'lettings/letting.html')
