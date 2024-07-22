from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the views.
        This method is executed once for the entire test case class.
        """
        cls.user = User.objects.create(username='testuser', password='password')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city='Test City')

    def test_index_view(self):
        """
        Test the index view to ensure it renders the correct template and context data.
        """
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn('profiles_list', response.context)
        self.assertContains(response, self.profile.user.username)

    def test_profile_view(self):
        """
        Test the profile view to ensure it renders the correct template and context data.
        """
        response = self.client.get(reverse('profiles_profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertIn('profile', response.context)
        self.assertContains(response, self.profile.user.username)
        self.assertContains(response, self.profile.favorite_city)
