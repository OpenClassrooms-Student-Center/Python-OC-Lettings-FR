from django.test import Client, TestCase
from django.urls import reverse


class TestOcLettingsSite(TestCase):

    def test_index_page_title_found(self):
        url = reverse('index')
        client = Client()
        response = client.get(url)
        self.assertContains(response, 'Holiday Homes')
