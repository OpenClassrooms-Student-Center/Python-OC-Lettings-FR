from django.test import TestCase, Client
from django.urls import reverse
from .models import Letting
from .models import Address


class lettingsPagesTests(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        address = Address.objects.create(
            number=74,
            street="Montreuil",
            city="Montreuil",
            state="ID",
            zip_code=93100,
            country_iso_code="FRA"
        )

        Letting.objects.create(
            title="Test Letting",
            address=address
        )

    def test_index_page(self):
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_page(self):
        response = self.client.get(reverse('letting', kwargs={'letting_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
