from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsViewsTests(TestCase):
    """
    Tests unitaires des vues de l'application Lettings.

    Vérifie que les pages de liste et de détail des locations
    répondent correctement et affichent les bonnes informations.
    """

    def setUp(self):
        """
        Initialise les données de test : une adresse et une location.

        Cette méthode est exécutée avant chaque test pour garantir
        un environnement de test cohérent.
        """
        self.address = Address.objects.create(
            number=123,
            street="Main street",
            city="Miami",
            state="Florida",
            zip_code=98210,
            country_iso_code="USA",
        )

        self.letting = Letting.objects.create(title="House", address=self.address)

    def test_lettings_index_view(self):
        """
        Vérifie que la page d’index des locations retourne un code 200
        et contient le titre de la location.
        """
        url = reverse("lettings:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "House")

    def test_lettings_detail_view(self):
        """
        Vérifie que la page de détail d’une location retourne un code 200
        et contient l’adresse de la location.
        """
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Main street")
