from django.urls import reverse


def test_index_get(client):
    response = client.get(reverse('index'))
    assert b"Welcome to Holiday Homes" in response.content
    assert response.status_code == 200
