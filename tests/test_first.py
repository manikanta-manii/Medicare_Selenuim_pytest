import time

from pages.login_page import TestLoginPage
from pages.admin_page import TestAdminPage
from database.doctors import DoctorsDB
from database.medicines import MedicinesDB
from conftest import chrome_browser

url = "http://localhost:3000/"
# medicine_image = "/Users/mparameswarappa/Downloads/dolo.jpg"
medicine_image = "/home/manikanta/Downloads/Doctors_Images"
delay = 3

def test_scenario_1(chrome_browser):
    driver = chrome_browser
    test_login = TestLoginPage(driver)
    test_login.login("admin@gmail.com", "Admin@123")
    test_add = TestAdminPage(driver)
    test_add.click_doctor_view()
    time.sleep(1)
    doctor1 = test_add.add_doctor("doctor1", "doctor1@gmail.com", "8987678987", "2", "1000", 1)
    time.sleep(1)
    doctor2 = test_add.add_doctor("doctor2", "doctor2@gmail.com", "9878987678", "3", "1500", 2)
    time.sleep(1)
    doctors_table = DoctorsDB()
    total_doctors = doctors_table.get_doctors_count()
    last_doctor_email = doctors_table.get_last_doctor_email()

    assert total_doctors == 2
    assert last_doctor_email == "doctor2@gmail.com"

    time.sleep(1)
    medicines_table = MedicinesDB()
    time.sleep(1)
    before_total_medicines = medicines_table.get_medicines_count()
    time.sleep(1)
    medicine1 = test_add.add_medicine(medicine_image, "DOLO", "FOR FEVER AND HEADACE", "10", "2", "10", "true")
    time.sleep(1)
    medicine2 = test_add.add_medicine(medicine_image, "PARACETAMOL", "FOR FEVER AND HEADACE", "10", "2", "10", "false")
    time.sleep(1)
    after_total_medicines = medicines_table.get_medicines_count()
    time.sleep(1)
    last_medicine_name = medicines_table.get_last_medicine_name()
    time.sleep(1)
    assert before_total_medicines == after_total_medicines - 2
    assert last_medicine_name == "PARACETAMOL"
