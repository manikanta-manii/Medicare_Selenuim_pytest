import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass
from selenium.webdriver.support.select import Select

url = "http://localhost:3000/medicines"


class TestBuyMedicinePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get(url)
        time.sleep(1)

    def add_to_cart(self,count):
        for i in range(1,count+1):
            BaseClass(self.driver, 3).wait_and_click((By.XPATH, f'(//button[@type="submit" and text()="Add to Cart"])[{i}]'))
            print("Medicine added to cart")
        time.sleep(1)
        self.driver.get("http://localhost:3000/order_items")

    def click_on_checkout(self):
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "//button[@type='button' and normalize-space()='checkout']"))

    def order_with_prescription(self,prescription):
        BaseClass(self.driver, 3).wait_and_send_keys((By.XPATH, '//input[@type="file"]'), prescription)
        time.sleep(1)
        BaseClass(self.driver, 3).wait_and_click((By.ID, "submitButton"))

    def order_without_prescription(self):
        BaseClass(self.driver, 3).wait_and_click((By.ID, "submitButton"))

    def remove_item_from_cart(self):
        self.driver.get("http://localhost:3000/order_items")
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, "(//button[normalize-space()='Remove'])[last()]"))
        self.driver.get("http://localhost:3000/order_items")












