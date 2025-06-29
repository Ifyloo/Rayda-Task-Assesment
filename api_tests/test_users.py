
import pytest
import requests

BASE_URL = "http://example.com/api"

@pytest.fixture
def user_payload():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }

def test_create_user(user_payload):
    response = requests.post(f"{BASE_URL}/users", json=user_payload)
    assert response.status_code == 201

def test_get_user():
    user_id = 1  # placeholder
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json().get("id") == user_id

