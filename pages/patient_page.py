import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass
from selenium.webdriver.support.select import Select

url = "http://localhost:3000/doctors"


class TestSlotBookPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get(url)
        time.sleep(1)

    def select_specalization(self, sid):
        print(sid)
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'specializationDropdown'))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, f"//label[@class='dropdown-item' and normalize-space()='{sid}']"))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "//input[@type='submit' and @value='Search']"))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "(//button[@type='submit' and text()='Book Appointment'])[1]"))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "//button[@id='tomo-btn']"))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "(//div[@id='current_slots']//button)[1]"))

        BaseClass(self.driver, 3).wait_and_send_keys((By.XPATH, "//textarea[@id ='appointmentReason']"), "I HAVE FEVER")
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "//input[@type='submit' and @value='Confirm']"))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "//button[@type='submit' and text()='Log out']"))


