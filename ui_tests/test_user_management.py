# test_user_management.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_create_user_via_ui():
    driver = webdriver.Chrome()
    driver.get("http://example.com/login")
    
    # Log in as admin
    driver.find_element(By.ID, "username").send_keys("admin_user")
    driver.find_element(By.ID, "password").send_keys("securePass123!")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    # Navigate to user management
    driver.find_element(By.LINK_TEXT, "User Management").click()
    time.sleep(1)
    
    # Create new user
    driver.find_element(By.ID, "add-user-button").click()
    driver.find_element(By.ID, "username").send_keys("emma.michaels")
    driver.find_element(By.ID, "email").send_keys("emma.michaels@example.com")
    driver.find_element(By.ID, "password").send_keys("emmaPass2025!")
    driver.find_element(By.ID, "save-button").click()
    time.sleep(2)
    
    # Verify success message
    assert "User created successfully" in driver.page_source
    
    driver.quit()

