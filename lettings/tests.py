from django.test import Client
from django.urls import reverse

import pytest

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_letting_index_uri():
    c = Client()
    lettings_index_uri = reverse('lettings_index')
    resp = c.get(lettings_index_uri)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_letting_index_title():
    c = Client()
    lettings_index_uri = reverse('lettings_index')
    resp = c.get(lettings_index_uri)
    assert b"<title>" in resp.content


@pytest.mark.django_db
def test_letting_uri():
    c = Client()

    adrs = Address.objects.create(
        number=1,
        street="aoîzfna",
        city="apozjoa",
        state="aokzd",
        zip_code=323,
        country_iso_code="FR1"
    )
    lting = Letting.objects.create(
        title='title',
        address=adrs,
    )

    letting_uri = reverse("letting", args=['1'])
    resp = c.get(letting_uri)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_letting_title():
    c = Client()

    adrs = Address.objects.create(
        number=1,
        street="aoîzfna",
        city="apozjoa",
        state="aokzd",
        zip_code=323,
        country_iso_code="FR1"
    )
    lting = Letting.objects.create(
        title='title',
        address=adrs,
    )

    letting_uri = reverse("letting", args=['1'])
    resp = c.get(letting_uri)
    assert b"<title>" in resp.content
