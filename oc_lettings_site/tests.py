from django.test import TestCase
# Import reload to force the URLconf to pick up the patched view
from importlib import reload
from django.urls import reverse, clear_url_caches
from django.test.utils import override_settings
from unittest.mock import patch
# Import the URLs module to be reloaded
import oc_lettings_site.urls as root_urlconf


class RootViewTest(TestCase):
    """Tests the main index view for the project."""

    def test_index_view_status_code_and_template(self):
        """Tests that the root index page loads correctly and uses the right template."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


# Use override_settings to ensure Django uses the root URLconf for custom handlers
@override_settings(ROOT_URLCONF='oc_lettings_site.urls')
class ErrorHandlerTest(TestCase):
    """Tests for the custom 404 and 500 error handlers."""

    def test_404_page_loads_and_returns_404_status(self):
        """
        Tests that a non-existent URL returns a 404 status code and uses the custom 404 template.
        """
        # Request a non-existent path to trigger the custom 404 handler
        response = self.client.get('/nonexistent-page-404/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    @patch(
        'oc_lettings_site.views.index',
        # Set a side effect that raises an Exception, which triggers the 500 handler
        side_effect=Exception('Intentional Server Crash for 500 Test')
    )
    # DEBUG=False is required for Django's custom error handlers to be called
    @override_settings(DEBUG=False)
    def test_500_page_loads_and_returns_500_status(self, mock_index):
        """
        Tests that an internal server error returns a 500 status code and uses the custom 500 template.
        """
        # Clear the URL cache
        clear_url_caches()

        # Reload the URLconf module to ensure the patched view is used
        reload(root_urlconf)

        # ✅ Prevent Django test client from re-raising exceptions
        self.client.raise_request_exception = False

        # Access the index URL, which now crashes and triggers the 500 handler
        response = self.client.get(reverse('index'))

        # Assert that the custom 500 handler was correctly executed
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, '500.html')
