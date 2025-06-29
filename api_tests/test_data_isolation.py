

import requests

BASE_URL = "http://example.com/api"

def test_admin_can_create_user():
    token = "admin_token"  
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "pass123"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code == 201

def test_user_cannot_create_user():
    token = "user_token"  
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "username": "anotheruser",
        "email": "anotheruser@example.com",
        "password": "pass123"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code == 403

