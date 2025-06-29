# test_input_validation.py

import requests

BASE_URL = "http://example.com/api"

def test_sql_injection_in_username():
    payload = {
        "username": "' OR '1'='1",
        "email": "inject@example.com",
        "password": "safePass123!"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code in [400, 422]

def test_xss_in_username():
    payload = {
        "username": "<script>alert('XSS')</script>",
        "email": "xss@example.com",
        "password": "cleanPass456!"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code in [400, 422]

