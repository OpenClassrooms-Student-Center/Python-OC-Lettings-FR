import pytest
from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


class LettingsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_code(self):
        response = self.client.get(reverse('lettings:index'))
        assert response.status_code == 200

    def test_view_title(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "Lettings")

    def test_view_particular_title(self):
        address = Address.objects.create(
            number=10,
            street="Rue du général",
            city="Bordeaux",
            state="Gironde",
            zip_code=33000,
            country_iso_code="isocode"
        )
        Letting.objects.create(title="LettingTest", address=address)
        response = self.client.get(reverse('lettings:letting', args=[1]))
        self.assertIn(b"<title>LettingTest</title>", response.content)
