from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfilesViewsTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Create a test profile
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )

    def test_index_view(self):
        """Test the profiles list view."""

        url = reverse('profiles:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn('profiles_list', response.context)
        self.assertEqual(len(response.context['profiles_list']), 1)
        self.assertEqual(response.context['profiles_list'][0], self.profile)

    def test_profile_view(self):
        """Test the profile detail view."""

        url = reverse('profiles:profile', args=[self.user.username])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)

    def test_profile_view_404(self):
        """Test the profile detail view with non-existent username."""

        url = reverse('profiles:profile', args=['nonexistentuser'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
