from django.test import Client, TestCase
from django.urls import reverse
from .models import (
    Address,
    Letting
)


class DataTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address1 = Address.objects.create(
            number=200,
            street='Ocean Street',
            city='New York',
            state='USA',
            country_iso_code='NY',
            zip_code=99,
        )
        cls.address2 = Address.objects.create(
            number=55,
            street='Avenue du Général De Gaulle',
            city='Strasbourg',
            state='France',
            country_iso_code='Alsace',
            zip_code=57,
        )
        cls.letting1 = Letting.objects.create(
            address=cls.address1,
            title='Home Sweet Home',
        )
        cls.letting2 = Letting.objects.create(
            address=cls.address2,
            title='Bienvenue en Alsace !!',
        )


class TestLettings(DataTest):
    def test_index(self):
        self.client = Client()
        url = reverse("lettings")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Lettings</title>')
        self.assertContains(response, self.letting1.title)
        self.assertContains(response, self.letting2.title)
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_letting(self):
        self.client = Client()
        url = reverse("letting", args=[self.letting1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'<title>{self.letting1.title}</title>')
        self.assertContains(response, self.letting1.address.street)
        self.assertTemplateUsed(response, "lettings/letting.html")
