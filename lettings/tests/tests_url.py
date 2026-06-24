"""
Tests module for lettings app urls
"""
import pytest

from django.urls import reverse, resolve

from lettings.models import Letting, Address


class TestLettingsUrl:
    def test_lettings_index_url(self):
        path = reverse(viewname="lettings:index")

        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings:index"

    @pytest.mark.django_db
    def test_lettings_letting_url(self, get_address: Address, get_letting: Letting):
        path = reverse(viewname="lettings:letting", kwargs={"letting_id": get_letting.id})

        assert path == "/lettings/1/"
        assert resolve(path).view_name == "lettings:letting"
