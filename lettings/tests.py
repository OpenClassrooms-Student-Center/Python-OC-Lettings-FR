from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingViewsTest(TestCase):

    def setUp(self) -> None:
        self.address = Address.objects.create(
            number=12,
            street="Rue de Strasbourg",
            city="Clermont-ferrand",
            state="Auvergne",
            zip_code=63000,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(address=self.address, title="Test Letting")

    def test_lettings_index(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, "<title>Lettings</title>")

    def test_lettings_infos_page(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, f"<title>{self.letting.title}</title>")
