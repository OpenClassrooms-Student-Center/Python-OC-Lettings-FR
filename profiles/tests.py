"""
Unit and integration tests for the 'profiles' application.

Covers:
- Models (Profile) data integrity and string representation.
- URL routing and resolution.
- Views functionality (index, detail) and template rendering.
"""
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """Tests for the Profile model."""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        cls.user = User.objects.create_user(
            username='jdoe',
            first_name='John',
            last_name='Doe',
            email='jdoe@test.com'
        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            favorite_city='Orange County'
        )

    def test_profile_model_content(self):
        """Tests the string representation and field values of the Profile model."""
        # This test ensures the missing line in models.py:__str__ is covered.
        self.assertEqual(str(self.profile), 'jdoe')
        self.assertEqual(self.profile.favorite_city, 'Orange County')
        self.assertEqual(self.profile.user.first_name, 'John')


class ProfileURLTest(TestCase):
    """Tests for the URL routing of the profiles application."""

    @classmethod
    def setUpTestData(cls):
        """Create a user and profile object to ensure the detail view URL is testable."""
        cls.user = User.objects.create_user(username='testuser')
        cls.profile = Profile.objects.create(user=cls.user)

    def test_index_url_resolves(self):
        """Tests that the '/profiles/' URL resolves to the correct view function ('profiles:index')."""
        url = reverse('profiles:index')
        # Check if the URL resolves to the view function named 'index'
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_profile_detail_url_resolves(self):
        """Tests that the '/profiles/<username>/' URL resolves to the correct view function ('profiles:profile')."""
        url = reverse('profiles:profile', args=[self.user.username])
        # Check if the URL resolves to the view function named 'profile'
        self.assertEqual(resolve(url).func.__name__, 'profile')


class ProfileViewTest(TestCase):
    """Tests for the views (functionality and rendering) of the profiles application."""

    @classmethod
    def setUpTestData(cls):
        """Create test data for views: two users and their profiles."""
        cls.user_a = User.objects.create_user(username='usera', first_name='A')
        cls.profile_a = Profile.objects.create(user=cls.user_a, favorite_city='City A')

        cls.user_b = User.objects.create_user(username='userb', first_name='B')
        cls.profile_b = Profile.objects.create(user=cls.user_b, favorite_city='City B')

    def test_index_view_status_code_and_template(self):
        """Tests that the profiles index page returns 200 and uses the correct template."""
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_index_view_content(self):
        """Tests that the index view context contains all profiles and their usernames are in the response."""
        response = self.client.get(reverse('profiles:index'))
        # Check if both profiles are in the context list
        self.assertIn(self.profile_a, response.context['profiles_list'])
        self.assertIn(self.profile_b, response.context['profiles_list'])
        # Check if the response contains the usernames
        self.assertContains(response, 'usera')
        self.assertContains(response, 'userb')

    def test_profile_detail_view_success(self):
        """Tests that a valid profile detail page returns 200 and uses the correct template."""
        response = self.client.get(reverse('profiles:profile', args=[self.user_a.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        # Check for username and favorite city content
        self.assertContains(response, 'usera')
        self.assertContains(response, 'City A')

    def test_profile_detail_view_not_found(self):
        """Tests that an invalid username returns a 404 status code."""
        response = self.client.get(reverse('profiles:profile', args=['nonexistentuser']))
        self.assertEqual(response.status_code, 404)