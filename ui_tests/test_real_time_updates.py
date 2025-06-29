# test_real_time_updates.py

from selenium import webdriver
import time

def test_real_time_notifications():
    driver = webdriver.Chrome()
    driver.get("http://example.com/dashboard")
    
    # Simulate waiting for a real-time notification
    time.sleep(5)  # assume backend pushes a notification here
    
    assert "New notification" in driver.page_source
    
    driver.quit()

