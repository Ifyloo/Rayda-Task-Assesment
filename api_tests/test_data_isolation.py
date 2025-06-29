# test_data_isolation.py

import requests

BASE_URL = "http://example.com/api"

def test_tenant_data_isolation():
    token_tenant1 = "tenant1_token"
    token_tenant2 = "tenant2_token"
    headers_tenant1 = {"Authorization": f"Bearer {token_tenant1}"}
    headers_tenant2 = {"Authorization": f"Bearer {token_tenant2}"}

    # Create user in tenant 1
    payload = {"username": "tenant1user", "email": "tenant1@example.com", "password": "pass"}
    response_create = requests.post(f"{BASE_URL}/users", json=payload, headers=headers_tenant1)
    assert response_create.status_code == 201
    user_id = response_create.json().get("id")

    # Try to access user from tenant 2
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers_tenant2)
    assert response.status_code in [403, 404]
