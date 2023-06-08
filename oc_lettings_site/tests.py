from django.test import Client, TestCase
from django.urls import reverse


class TestSite(TestCase):
    def test_index(self):
        self.client = Client()
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Holiday Homes</title>')
        self.assertContains(response, f'<a href="{reverse("profiles")}">Profiles</a')
        self.assertContains(response, f'<a href="{reverse("lettings")}">Lettings</a')
        self.assertTemplateUsed(response, "oc_lettings_site/index.html")
