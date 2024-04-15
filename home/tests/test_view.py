from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest

from home.views import index


class TestIndexView(TestCase):
    def _extracted_from_test_returns_200_status_code_for_get_request_3(self):
        url = reverse('home:index')
        request = HttpRequest()
        return self.client.get(url)

    #  Returns a 200 status code for a GET request
    def test_handles_get_requests(self):
        # Arrange
        from django.shortcuts import render
        request = type('Request', (), {})()

        # Act
        response = index(request)

        # Assert
        assert response.status_code == 200

    def test_handles_post_requests(self):
        # Arrange
        from django.shortcuts import render
        request = type('Request', (), {})()
        request.method = 'POST'

        # Act
        response = index(request)

        # Assert
        assert response.status_code == 200

    #  Renders the 'home/index.html' template for a GET request
