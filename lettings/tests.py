from django.test import Client, TestCase
from django.urls import reverse

from .models import Address, Letting


class TestLettings(TestCase):

    def test_index_page_title_found(self):
        url = reverse('lettings_index')
        client = Client()
        response = client.get(url)
        self.assertContains(response, 'Lettings')

    def test_letting_page_title_found(self):
        address = Address.objects.create(number='123', street='street name', city='city name',
                                         state='NY', zip_code='12345', country_iso_code='USA')
        letting = Letting.objects.create(title='lettingTitle', address=address)
        url = reverse('letting', args=[letting.id])
        client = Client()
        response = client.get(url)
        self.assertContains(response, 'lettingTitle')
