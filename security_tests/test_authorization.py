# test_authorization.py

import requests

BASE_URL = "http://example.com/api"

def test_user_cannot_delete_other_user():
    user_token = "regular_user_token"  # placeholder
    headers = {"Authorization": f"Bearer {user_token}"}
    user_id_to_delete = 2  # assuming this user doesn't belong to current user
    
    response = requests.delete(f"{BASE_URL}/users/{user_id_to_delete}", headers=headers)
    assert response.status_code in [403, 401]

