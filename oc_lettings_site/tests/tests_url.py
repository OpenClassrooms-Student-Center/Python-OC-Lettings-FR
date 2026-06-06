"""
Tests module for oc_lettings_site app urls
"""
from django.urls import reverse, resolve


class TestOcLettingsSiteUrl:
    def test_index_url(self):
        """
        Method to test if the index url is accessible
        """
        path = reverse("index")

        assert path == "/"
        assert resolve(path).view_name == 'index'
