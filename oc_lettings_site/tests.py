from django.test import Client
from django.urls import reverse

c = Client()


home_uri = reverse('home')


def test_home_uri():
    resp = c.get(home_uri)
    assert resp.status_code == 200


def test_home_title():
    response = c.get(home_uri)
    assert b"<title>Holiday Homes</title>" in response.content
