import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass

url = "http://localhost:3000/doctors"

class TestSlotBookPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get(url)
        time.sleep(1)

    def select_specalization(self, sid):
        print(sid)
        base_class = BaseClass(self.driver, 3)
        base_class.wait_and_click((By.ID, 'specializationDropdown'))
        base_class.wait_and_click((By.XPATH, f"//label[@class='dropdown-item' and normalize-space()='{sid}']"))
        base_class.wait_and_click((By.XPATH, "//input[@type='submit' and @value='Search']"))
        base_class.wait_and_click((By.XPATH, "(//button[@type='submit' and text()='Book Appointment'])[1]"))
        base_class.wait_and_click((By.XPATH, "//button[@id='tomo-btn']"))
        base_class.wait_and_click((By.XPATH, "(//div[@id='current_slots']//button)[1]"))

        # button = self.driver.find_element(By.XPATH, "//textarea[@id ='appointmentReason']")
        # self.driver.implicitly_wait(10)
        # ActionChains(self.driver).move_to_element(button).send_keys("I HAVE FEVER").perform()
        # time.sleep(1)

        base_class.wait_and_send_keys((By.XPATH, "//textarea[contains(@placeholder,'appointment')]"), "I HAVE FEVER")
        base_class.wait_and_click((By.XPATH, "//input[@type='submit' and @value='Confirm']"))
        base_class.wait_and_click((By.XPATH, "//button[@type='submit' and text()='Log out']"))


