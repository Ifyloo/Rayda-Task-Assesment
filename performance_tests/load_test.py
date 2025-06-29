# load_test.py

from locust import HttpUser, task, between

class UserLoadTest(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_users(self):
        self.client.get("/api/users")

    @task
    def create_user(self):
        payload = {
            "username": "loaduser1",
            "email": "loaduser1@example.com",
            "password": "LoadPass123!"
        }
        self.client.post("/api/users", json=payload)

