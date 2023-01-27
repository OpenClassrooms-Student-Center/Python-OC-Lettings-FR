from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Profile


class TestProfiles(TestCase):

    def test_index_page_title_found(self):
        url = reverse('profiles_index')
        client = Client()
        response = client.get(url)
        self.assertContains(response, 'Profiles')

    def test_profile_page_title_found(self):
        user = User.objects.create(username='user', password='password')
        Profile.objects.create(user=user, favorite_city='new york')
        url = reverse('profile', args=[user.username])
        client = Client()
        response = client.get(url)
        self.assertContains(response, 'user')
