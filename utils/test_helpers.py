# utils/test_helpers.py

def print_response_details(response):
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

