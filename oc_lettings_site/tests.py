from django.test import TestCase, Client
from django.urls import reverse


class OCLettingsSiteViewsTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()

    def test_index_view(self):
        """Test the index view."""
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_404_view(self):
        """Test the 404 error view."""
        url = reverse('test_404')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_500_view(self):
        """Test the 500 error view."""
        url = reverse('test_500')
        with self.assertRaises(ZeroDivisionError):
            self.client.get(url)


def test_dummy():
    assert 1
