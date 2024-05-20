from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BaseClass:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay

    def wait_and_click(self, locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(locator))
        element.click()

    def wait_and_send_keys(self, locator, keys):
        element = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(locator))
        element.send_keys(keys)