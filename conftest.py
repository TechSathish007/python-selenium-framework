import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# 1. We create a custom terminal command called "--browser"
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def driver(request):
    # 2. We ask Pytest which browser the user typed in the terminal
    browser_name = request.config.getoption("--browser")
    
    # 3. We use an IF statement to launch the correct one!
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        
    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
        
    # 4. Hand the browser to the test
    yield driver
    
    # 5. Quit when finished
    driver.quit()