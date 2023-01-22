from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Profile


class ProfileViewsTest(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="Oc-lettings-test-User",
            password="user_pass",
            email="test-User@email.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city='Brisbane')

    def test_profiles_index(self):
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, "<title>Profiles</title>")

    def test_profiles_infos_page(self):
        url = reverse('profiles:profile', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, f"<title>{self.user.username}</title>")
