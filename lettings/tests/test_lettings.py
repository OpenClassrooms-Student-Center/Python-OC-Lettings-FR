from django.test import Client, SimpleTestCase
from django.conf import settings
from django.urls import reverse
import unittest


class TestLettings(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.simple_case = SimpleTestCase()

    def test_list_letting(self):
        url = reverse('lettings:index')
        self.assertEqual(url, '/lettings/')
        response = self.client.get(url)
        title_list = response.context['lettings_list']
        print(f'Lettings: Test three >>> {title_list}, Done ')

    def test_index_lettings(self):
        # Issue a GET request.
        url = reverse('lettings:index')
        self.assertEqual(url, '/lettings/')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check Title in index
        self.simple_case.assertContains(response, '<h1>Lettings</h1>')
        print(f'Lettings: Test one >>>  {url}, Done')

    def test_lettings_details(self):
        # Get response Request
        url = reverse('lettings:letting', kwargs={'letting_id': 1})
        self.assertEqual(url, '/lettings/1/')

        # create repsonse for the result
        response = self.client.get(url)

        # Check if the title correspond with the letting's id
        self.simple_case.assertContains(response, '<h1>Joshua Tree Green Haus /w Hot Tub</h1>')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        print(f'Lettings: Test two >>> {url} , Done')

    def test_lettings_details_context(self):
        url = reverse('lettings:letting', kwargs={'letting_id': 1})
        self.assertEqual(url, '/lettings/1/')
        response = self.client.get(url)
        title_list = response.context['title']
        print(f'Lettings: Test four >>> {title_list}, Done ')

    def test_language_using_cookie(self):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.simple_case.assertContains(response, '<h1>Lettings</h1>')
        print('Lettings: Test five Done')
