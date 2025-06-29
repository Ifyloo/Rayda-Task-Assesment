# test_authentication.py

import requests

BASE_URL = "http://example.com/api"

def test_invalid_token_access():
    headers = {"Authorization": "Bearer invalidtoken123"}
    response = requests.get(f"{BASE_URL}/users", headers=headers)
    assert response.status_code == 401

def test_missing_token_access():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 401

