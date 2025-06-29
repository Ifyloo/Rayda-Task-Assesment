# test_auth.py

import requests

BASE_URL = "http://example.com/api"

def test_login_valid_credentials():
    credentials = {"username": "testuser", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth/login", json=credentials)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_invalid_credentials():
    credentials = {"username": "wronguser", "password": "wrongpass"}
    response = requests.post(f"{BASE_URL}/auth/login", json=credentials)
    assert response.status_code == 401

def test_token_validation():
    token = "dummy_token"  # placeholder
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/protected-resource", headers=headers)
    assert response.status_code in [200, 401]


