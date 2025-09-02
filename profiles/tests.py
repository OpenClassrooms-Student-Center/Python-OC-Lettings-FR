from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class ProfilesTests(TestCase):
    """
    Tests unitaires des vues de l'application Profiles.

    Vérifie que les pages de liste et de détail des profils
    répondent correctement et affichent les bonnes informations.
    """

    def setUp(self):
        """
        Initialise un utilisateur et son profil associé pour les tests.

        Crée un utilisateur nommé 'dan' et un profil avec Paris comme ville favorite.
        """
        self.user = User.objects.create_user(username="dan", password="1234")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_index_view(self):
        """
        Vérifie que la page d’index des profils retourne un code 200
        et contient le mot 'Profiles'.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profiles")

    def test_profile_detail_view(self):
        """
        Vérifie que la page de détail d’un profil retourne un code 200
        et contient la ville favorite du profil.
        """
        response = self.client.get(
            reverse("profiles:profile", args=[self.user.username])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paris")
