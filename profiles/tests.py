"""
Unit tests for the profiles app.

This module contains test cases for models, views and urls of the profiles application.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestProfiles(TestCase):
    """Test class for profiles app."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username="test_user",
            first_name="Test",
            last_name="User",
            email="test@test.com",
            password="test_password"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Test City"
        )

    def test_profile_str_method(self):
        """Test the string representation of Profile model."""
        self.assertEqual(str(self.profile), self.user.username)

    def test_profiles_index_view(self):
        """Test the index view of profiles app."""
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Profiles", str(response.content))
        self.assertEqual(response.templates[0].name, 'profiles/index.html')

    def test_profile_detail_view(self):
        """Test the detail view of a profile."""
        url = reverse('profiles:profile', kwargs={'username': self.user.username})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user.username, str(response.content))
        self.assertEqual(response.templates[0].name, 'profiles/profile.html')

    def test_profile_detail_view_404(self):
        """Test the detail view with invalid username."""
        url = reverse('profiles:profile', kwargs={'username': 'invalid_user'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'profiles/profile.html')
