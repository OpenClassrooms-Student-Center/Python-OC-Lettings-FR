from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class DataTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(
            first_name='Dark',
            last_name='Vador',
            email="empire@starwars.com",
            username="Tonperre"
        )
        cls.profile1 = Profile.objects.create(
            user=cls.user1,
            favorite_city='London'
        )
        cls.user2 = User.objects.create(
            first_name='Luke',
            last_name='Skywalker',
            email="rebel@starwars.com",
            username="Tatouine"
        )
        cls.profile2 = Profile.objects.create(
            user=cls.user2,
            favorite_city='Barcelona'
        )


class TestProfiles(DataTest):
    def test_index(self):
        self.client = Client()
        url = reverse("profiles")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Profiles</title>')
        self.assertContains(response, self.profile1.user.username)
        self.assertContains(response, self.profile2.user.username)
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profile(self):
        self.client = Client()
        url = reverse("profile", args=[self.profile1.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'<title>{self.profile1.user.username}</title>')
        self.assertContains(response, self.profile1.user.email)
        self.assertContains(response, self.profile1.favorite_city)
        self.assertTemplateUsed(response, "profiles/profile.html")
