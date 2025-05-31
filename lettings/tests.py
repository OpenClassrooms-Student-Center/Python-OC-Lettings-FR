from django.test import TestCase, Client
from django.urls import reverse
from .models import Letting, Address


class LettingViewsTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="FR"
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_index_view(self):
        """Test the index view."""
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn('lettings_list', response.context)
        self.assertEqual(len(response.context['lettings_list']), 1)
        self.assertEqual(response.context['lettings_list'][0], self.letting)

    def test_letting_view(self):
        """Test the letting detail view."""
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.letting.address)

    def test_letting_view_404(self):
        """Test the letting detail view with non-existent letting."""
        url = reverse('lettings:letting', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
