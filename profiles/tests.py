from django.test import TestCase, Client
from django.urls import reverse
from .models import User
from .models import Profile


class profilesPagesTests(TestCase):

    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        # Créer une instance de Address
        user = User.objects.create_user(
                                        username='testuser',
                                        first_name='test',
                                        last_name='user',
                                        email='testuser@example.com',
                                        password='testpassword'
                                        )
        Profile.objects.create(user=user, favorite_city='Montreuil')

    def test_index_page(self):
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_page(self):
        response = self.client.get(reverse('profile', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
