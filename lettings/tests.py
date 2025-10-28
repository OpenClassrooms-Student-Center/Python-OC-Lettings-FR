"""
Unit and integration tests for the 'lettings' application.

Covers:
- Models (Letting, Address) data integrity and string representation.
- URL routing and resolution.
- Views functionality (index, detail) and template rendering.
"""
from django.test import TestCase
from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404
from lettings.models import Address, Letting


class LettingModelTest(TestCase):
    """Tests for the Address and Letting models."""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        cls.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TCO'
        )
        cls.letting = Letting.objects.create(
            title='Test Letting Title',
            address=cls.address
        )

    def test_address_model_content(self):
        """Tests the string representation and field values of the Address model."""
        self.assertEqual(str(self.address), '123 Test Street')
        self.assertEqual(self.address.city, 'Test City')
        self.assertEqual(self.address.state, 'TS')

    def test_letting_model_content(self):
        """Tests the string representation and field values of the Letting model."""
        self.assertEqual(str(self.letting), 'Test Letting Title')
        self.assertEqual(self.letting.title, 'Test Letting Title')
        self.assertEqual(self.letting.address.street, 'Test Street')


class LettingURLTest(TestCase):
    """Tests for the URL routing of the lettings application."""

    @classmethod
    def setUpTestData(cls):
        """Create a letting object to ensure the detail view URL is testable."""
        cls.address = Address.objects.create(
            number=456, street='URL Street', city='URL City', state='UC', zip_code=67890, country_iso_code='UCO'
        )
        cls.letting = Letting.objects.create(title='URL Test Letting', address=cls.address)

    def test_index_url_resolves(self):
        """Tests that the '/lettings/' URL resolves to the correct view function ('lettings:index')."""
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_letting_detail_url_resolves(self):
        """Tests that the '/lettings/<id>/' URL resolves to the correct view function ('lettings:letting')."""
        url = reverse('lettings:letting', args=[self.letting.id])
        self.assertEqual(resolve(url).func.__name__, 'letting')


class LettingViewTest(TestCase):
    """Tests for the views (functionality and rendering) of the lettings application."""

    @classmethod
    def setUpTestData(cls):
        """Create test data for views: two lettings."""
        cls.address_1 = Address.objects.create(
            number=1, street='First St', city='A City', state='AC', zip_code=10000, country_iso_code='USA'
        )
        cls.letting_1 = Letting.objects.create(title='Letting A', address=cls.address_1)

        cls.address_2 = Address.objects.create(
            number=2, street='Second St', city='B City', state='BC', zip_code=20000, country_iso_code='USA'
        )
        cls.letting_2 = Letting.objects.create(title='Letting B', address=cls.address_2)

    def test_index_view_status_code(self):
        """Tests that the lettings index page returns a 200 status code."""
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        """Tests that the lettings index page uses the correct template."""
        response = self.client.get(reverse('lettings:index'))
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_index_view_content(self):
        """Tests that the index view context contains all lettings and their titles are in the response."""
        response = self.client.get(reverse('lettings:index'))
        # Check if the list contains both lettings
        self.assertIn(self.letting_1, response.context['lettings_list'])
        self.assertIn(self.letting_2, response.context['lettings_list'])
        # Check if the response contains the titles
        self.assertContains(response, 'Letting A')
        self.assertContains(response, 'Letting B')

    def test_letting_detail_view_success(self):
        """Tests that a valid letting detail page returns a 200 status code and uses the correct template."""
        response = self.client.get(reverse('lettings:letting', args=[self.letting_1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        # Check if the title is present
        self.assertContains(response, 'Letting A')
        # Check if the address content is present
        self.assertContains(response, 'First St')

    def test_letting_detail_view_not_found(self):
        """Tests that an invalid letting ID returns a 404 status code."""
        # Assume max existing ID is self.letting_2.id
        invalid_id = self.letting_2.id + 1
        response = self.client.get(reverse('lettings:letting', args=[invalid_id]))
        self.assertEqual(response.status_code, 404)