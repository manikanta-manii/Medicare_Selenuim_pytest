import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='module', autouse=True)
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
