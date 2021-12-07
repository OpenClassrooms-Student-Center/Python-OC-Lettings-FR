from django.test import TestCase
from django.urls import reverse

class TestView(TestCase):
    def test_view_code(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200

    def test_view_title(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Welcome to Holiday Homes")