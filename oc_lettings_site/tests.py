from django.test import TestCase, Client
from django.test.utils import override_settings
from django.urls import reverse
from lettings.models import Letting, Address
from profiles.models import Profile
from django.contrib.auth.models import User


class ErrorPagesTests(TestCase):

    def setUp(self):
        # Client est une instance de classe pour faire des requêtes de test
        self.client = Client()

    @override_settings(DEBUG=False)
    def test_404_error_page(self):
        # Fait une requête à une URL qui n'existe pas
        response = self.client.get('/nonsense')
        # Vérifie que la réponse est bien une erreur 404
        self.assertEqual(response.status_code, 404)
        # Vérifie que le bon template est utilisé pour la page 404
        self.assertTemplateUsed(response, 'oc_lettings_site/404.html')

    @override_settings(DEBUG=False)
    def test_500_error_page(self):
        response = self.client.get(reverse('get_500'))
        self.assertEqual(response.status_code, 500)


class IndexPageTests(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        # Créer une instance de Address
        address = Address.objects.create(
            number=74,
            street="rue Carnot",
            city="Montreuil",
            state="ID",
            zip_code=93100,
            country_iso_code="FRA"
        )

        Letting.objects.create(
            title="Test Letting",
            address=address
        )

        user = User.objects.create_user(
                                        first_name='test',
                                        last_name='user',
                                        username='testuser',
                                        email='testuser@example.com',
                                        password='testpassword'
                                        )
        Profile.objects.create(user=user, favorite_city='Montreuil')

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')

    def test_functionnal_check_lettings(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
        self.assertContains(response, 'href="/lettings/"')
        self.assertContains(response, 'Lettings')

        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, 'href="/lettings/1/"')
        self.assertContains(response, 'Test Letting')

        response = self.client.get(reverse('letting', kwargs={'letting_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

        # print(response.content.decode('utf-8'))
        self.assertContains(response, 'Test Letting', html=True)
        self.assertContains(response, '<p>74 rue Carnot</p>', html=True)
        self.assertContains(response, '<p>Montreuil, ID 93100</p>', html=True)
        self.assertContains(response, '<p>FRA</p>', html=True)

    def test_functionnal_check_profiles(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
        self.assertContains(response, 'href="/profiles/"')
        self.assertContains(response, 'Profiles')
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        response = self.client.get(reverse('profile', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'testuser', html=True)
        # print(response.content.decode('utf-8'))
        self.assertContains(response, '<p><strong>First name :</strong> test</p>', html=True)
        self.assertContains(response, '<p><strong>Last name :</strong> user</p>', html=True)
        self.assertContains(
                            response,
                            '<p><strong>Email :</strong> testuser@example.com</p>',
                            html=True
                            )
        self.assertContains(
                            response,
                            '<p><strong>Favorite city :</strong> Montreuil</p>',
                            html=True
                            )
