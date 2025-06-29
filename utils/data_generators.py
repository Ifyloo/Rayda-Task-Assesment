# utils/data_generators.py

import random
import string

def generate_random_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=6))

def generate_random_email():
    return generate_random_username() + "@example.com"

