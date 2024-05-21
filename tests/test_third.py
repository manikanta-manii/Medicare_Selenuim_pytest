import time

from pages.login_page import TestLoginPage
from pages.medicine_page import TestBuyMedicinePage
from conftest import chrome_browser
from database.medicines import MedicinesDB
from database.orders import OrdersDB

url = "http://localhost:3000/"
medicine_image = "/Users/mparameswarappa/Downloads/dolo.jpg"
# medicine_image = "/home/manikanta/Downloads/Doctors_Images/medicine.jpg"

def test_scenario_3(chrome_browser):
    driver = chrome_browser
    test_login = TestLoginPage(driver)
    test_login.login("manikantap036@gmail.com", "Abcd@123")
    time.sleep(1)

    test_medicine = TestBuyMedicinePage(driver)
    test_medicine.navigate_to_url()
    #
    medicines_table = MedicinesDB()
    time.sleep(1)
    total_medicines = medicines_table.get_medicines_count()
    test_medicine.add_to_cart(total_medicines)
    test_medicine.click_on_checkout()
    test_medicine.order_without_prescription()
    time.sleep(1)
    orders_table = OrdersDB()
    first_order_status = orders_table.get_status()
    assert first_order_status == False

    time.sleep(1)
    test_medicine.remove_item_from_cart()
    test_medicine.click_on_checkout()
    test_medicine.order_without_prescription()
    time.sleep(1)
    second_order_status = orders_table.get_status()
    assert second_order_status == True

    test_medicine.navigate_to_url()
    test_medicine.add_to_cart(total_medicines)
    test_medicine.click_on_checkout()
    test_medicine.order_with_prescription(medicine_image)
    time.sleep(2)
    third_order_status = orders_table.get_status()
    assert third_order_status == True
