import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # 1. Set up Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--headless") # This makes it invisible!
    chrome_options.add_argument("--window-size=1920,1080") # Gives it a virtual screen size
    
    # 2. Launch Chrome invisibly
    driver = webdriver.Chrome(options=chrome_options)
    
    # 3. Hand the invisible browser to the test
    yield driver
    
    # 4. Quit when finished
    driver.quit()