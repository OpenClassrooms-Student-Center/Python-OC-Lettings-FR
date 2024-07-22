from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from lettings.models import Letting, Address


class LettingsViewsTests(TestCase):

    def setUp(self):
        """
        Set up test data for the views.
        """
        self.user = User.objects.create(username='testuser', password='password')
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(title='Test Letting', address=self.address)

    def test_index_view(self):
        """
        Test the index view to ensure it renders the correct template and context data.
        """
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn('lettings_list', response.context)
        self.assertContains(response, self.letting.title)

    def test_letting_view(self):
        """
        Test the letting view to ensure it renders the correct template and context data.
        """
        response = self.client.get(reverse('lettings_letting', args=[self.letting.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertIn('title', response.context)
        self.assertIn('address', response.context)
        self.assertContains(response, self.letting.title)
        self.assertContains(response, self.address.street)
