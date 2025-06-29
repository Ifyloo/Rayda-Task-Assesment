# test_responsive_design.py

from selenium import webdriver

def test_responsive_layout():
    driver = webdriver.Chrome()
    
    # Desktop size
    driver.set_window_size(1200, 800)
    driver.get("http://example.com/dashboard")
    assert "Dashboard" in driver.title
    
    # Mobile size
    driver.set_window_size(375, 667)
    driver.get("http://example.com/dashboard")
    assert "Dashboard" in driver.title
    
    driver.quit()

