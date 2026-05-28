"""
Tests module for oc_lettings_site app views
"""
import pytest

from django.template.response import TemplateResponse
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from _pytest.monkeypatch import MonkeyPatch


class TestOcLettingsSiteView:
    @pytest.mark.django_db
    def test_oc_lettings_site_index_view_ok(self):
        client = Client()
        path = reverse(viewname="index")

        response = client.get(path=path)
        content = response.content.decode()
        expected = "Welcome to Holiday Homes"

        assert expected in content
        assert response.status_code == 200
        assertTemplateUsed(response, template_name="index.html")

    @pytest.mark.django_db
    def test_oc_lettings_site_index_view_returns_500(self, monkeypatch: MonkeyPatch):
        def side_effect(request, template_name, context=None, status=500):
            if template_name == "index.html":
                raise Exception("forced error")
            return TemplateResponse(request, template_name, context or {}, status=status)

        monkeypatch.setattr("oc_lettings_site.views.render", side_effect)

        client = Client()
        path = reverse(viewname="index")

        response = client.get(path=path)
        content = response.content.decode()
        expected_h1 = (f'<h1 class="page-header-ui-title mb-3 display-6">500 Error : '
                       f'something wrong with the server - forced error</h1>')

        assert expected_h1 in content
        assert response.status_code == 500
        assertTemplateUsed(response, template_name="error_500.html")
