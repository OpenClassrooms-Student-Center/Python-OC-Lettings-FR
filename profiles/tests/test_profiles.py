from django.test import Client, SimpleTestCase
from django.urls import reverse
import unittest
from django.conf import settings


class TestProfiles(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.simple_case = SimpleTestCase()

    def test_list_letting(self):
        url = reverse('profiles:index')
        self.assertEqual(url, '/profiles/')
        response = self.client.get(url)
        title_list = response.context['profiles_list']
        print(f'Profile :Test one >>> {title_list}, Done ')

    def test_index_lettings(self):
        # Issue a GET request.
        url = reverse('profiles:index')
        self.assertEqual(url, '/profiles/')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check Title in index
        self.simple_case.assertContains(response, '<h1>Profiles</h1>')
        print(f'Profile :Test two >>>  {url}, Done')

    def test_lettings_details(self):
        # Get response Request
        url = reverse('profiles:profile', kwargs={'username': str('HeadlinesGazer')})
        self.assertEqual(url, '/profiles/HeadlinesGazer/')

        # create repsonse for the result
        response = self.client.get(url)

        # Check if the title correspond with the letting's id
        self.simple_case.assertContains(response, '<h1>HeadlinesGazer</h1>')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        print(f'Profile :Test three >>> {url} , Done')

    def test_lettings_details_context(self):
        url = reverse('profiles:profile', kwargs={'username': str('HeadlinesGazer')})
        self.assertEqual(url, '/profiles/HeadlinesGazer/')
        response = self.client.get(url)
        title_list = response.context['profile']
        print(f'Profile :Test four >>> {title_list}, Done ')

    def test_language_using_cookie(self):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.simple_case.assertContains(response, '<h1>Profiles</h1>')
        print('Profile :Test five Done')
