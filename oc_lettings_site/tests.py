from django.test import TestCase
from django.urls import reverse


class MainViewsTests(TestCase):

    def test_index_view(self):
        """
        Test the index view to ensure it renders the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
