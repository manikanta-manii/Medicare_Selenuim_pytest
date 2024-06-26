
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass


class TestLoginPage:

    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit"]')

    def __init__(self,driver):
        self.driver=driver

    def login(self,user_email,user_password):
        self.driver.get("http://localhost:3000/users/sign_in/")
        self.driver.maximize_window()
        base_class = BaseClass(self.driver, 3)
        base_class.wait_and_send_keys((By.ID, 'user_email'),user_email)
        base_class.wait_and_send_keys((By.ID, 'user_password'), user_password)
        base_class.wait_and_click((By.XPATH, '//input[@type="submit"]'))
        print("1 .Successfully Login as Admin !")
