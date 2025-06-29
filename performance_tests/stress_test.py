
# stress_test.py

from locust import HttpUser, task, constant

class UserStressTest(HttpUser):
    wait_time = constant(0.5)
    
    @task
    def rapid_user_creation(self):
        payload = {
            "username": "stressuser99",
            "email": "stressuser99@example.com",
            "password": "StressPass2025!"
        }
        self.client.post("/api/users", json=payload)
