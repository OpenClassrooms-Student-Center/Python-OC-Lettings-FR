"""
Tests module for lettings app views
"""
import pytest

from django.urls import reverse
from django.test import Client, override_settings
from pytest_django.asserts import assertTemplateUsed
from _pytest.monkeypatch import MonkeyPatch

from lettings.models import Letting, Address


class TestLettingsView:
    @pytest.mark.django_db
    def test_lettings_index_view_ok(self, get_letting: Letting):
        """
        Method to test that index view returns 200
        Args:
            get_letting (Letting): a letting object
        """
        client = Client()
        path = reverse(viewname="lettings:index")

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = "Lettings"
        expected_content = f'<a href="/lettings/{get_letting.id}/">{get_letting.title}</a>'

        assert expected_h1 in content
        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, template_name="lettings/index.html")

    @pytest.mark.django_db
    def test_lettings_index_view_returns_500(self, monkeypatch: MonkeyPatch, get_letting: Letting):
        """
        Method to test that index view returns 500 in a server error case
        Args:
            monkeypatch (MonkeyPatch): a MonkeyPatch object
            get_letting (Letting): a letting object
        """
        def raise_error():
            raise Exception("forced error")

        monkeypatch.setattr("lettings.views.Letting.objects.all", raise_error)

        client = Client()
        client.raise_request_exception = False
        path = reverse(viewname="lettings:index")

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = "Internal Error : something wrong with the server !</h1>"

        assert expected_h1 in content
        assert response.status_code == 500
        assertTemplateUsed(response, template_name="oc_lettings_site/500.html")

    @pytest.mark.django_db
    def test_lettings_letting_view_ok(self, get_address: Address, get_letting: Letting):
        """
        Method to test that lettings index view returns 200
        Args:
            get_address (Address): an address object
            get_letting (Letting): a letting object
        """
        client = Client()
        path = reverse(viewname="lettings:letting", kwargs={"letting_id": get_letting.id})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = f"{get_letting.title}"
        expected_content = [f'{get_address.number} {get_address.street}',
                            f'{get_address.city}, {get_address.state}',
                            f'{get_address.zip_code}',
                            f'{get_address.country_iso_code}']

        assert expected_h1 in content
        for expected_child in expected_content:
            assert expected_child in content
        assert response.status_code == 200
        assertTemplateUsed(response, template_name="lettings/letting.html")

    @override_settings(DEBUG=False)
    @pytest.mark.django_db
    def test_lettings_letting_view_returns_404(self, get_address: Address, get_letting: Letting):
        """
        Method to test that letting index view returns 404 in case of 404 error
        Args:
            get_address (Adress): an address object
            get_letting (Letting): a letting object
        """
        client = Client()
        path = reverse(viewname="lettings:letting", kwargs={"letting_id": 2})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = f"404 Error : letting n\xb0 2 not found !</h1>"

        assert expected_h1 in content
        assert response.status_code == 404
        assertTemplateUsed(response, template_name="oc_lettings_site/404.html")

    @pytest.mark.django_db
    def test_lettings_letting_view_returns_500(self,
                                               monkeypatch: MonkeyPatch,
                                               get_letting: Letting):
        """
        Method to test that letting index view returns 500 in case of 500 error
        Args:
            monkeypatch (MonkeyPatch): a MonkeyPatch object
            get_letting (Letting): a letting object
        """
        def raise_error(*args, **kwargs):
            raise Exception("forced error")

        monkeypatch.setattr("lettings.views.get_object_or_404", raise_error)

        client = Client()
        client.raise_request_exception = False
        path = reverse(viewname="lettings:letting", kwargs={"letting_id": get_letting.id})

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = "Internal Error : something wrong with the server !"

        assert expected_h1 in content
        assert response.status_code == 500
        assertTemplateUsed(response, template_name="oc_lettings_site/500.html")
