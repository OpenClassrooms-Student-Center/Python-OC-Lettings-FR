from django.test import Client, SimpleTestCase
from django.urls import reverse
import unittest


class TestIndex(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.simple_case = SimpleTestCase()

    def test_list_letting(self):
        url = reverse('index')
        self.assertEqual(url, '/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.simple_case.assertContains(response, '<h1>Welcome to Holiday Homes</h1>')

        print('Index : Test One pass ... Great')
