import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


def test_healthcheck(api_client):
    response = api_client.get("/health/")
    assert response.status_code == 200
