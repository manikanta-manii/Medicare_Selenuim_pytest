import time
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass

url="http://localhost:3000/appointments"

class TestDoctorPage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get(url)
        time.sleep(1)
    def click_on_view(self):
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "(//button[@type='submit' and text()='View Details'])[last()]"))
        time.sleep(1)

    def prescribe(self):
        base_class = BaseClass(self.driver, 3)
        base_class.wait_and_click((By.XPATH, "//button[@type='button' and normalize-space()='Prescribe']"))
        base_class.wait_and_send_keys((By.XPATH, "//trix-editor"), "DOLO 650 , Paracetamol")
        base_class.wait_and_click((By.XPATH, "//input[@type='submit' and @value='Submit']"))
        base_class.wait_and_click((By.XPATH, "//button[@type='submit'and text()='Complete Appointment']"))
        base_class.wait_and_click((By.XPATH, "//button[@type='submit' and text()='Log out']"))


