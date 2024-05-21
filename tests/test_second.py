import time

from pages.login_page import TestLoginPage
from pages.patient_page import TestSlotBookPage
from pages.doctor_page import TestDoctorPage
from conftest import chrome_browser
from pages.admin_page import TestAdminPage
from database.appointments import AppointmentsDB
from database.medicines import MedicinesDB

url="http://localhost:3000/"
medicine_image="/Users/mparameswarappa/Downloads/dolo.jpg"


# def test_scenario_2(chrome_browser):
    # driver = chrome_browser
    # test_login = TestLoginPage(driver)
    # test_login.login("manikantap036@gmail.com","Abcd@123")
    # time.sleep(1)
    #
    # test_slot_book = TestSlotBookPage(driver)
    # test_slot_book.navigate_to_url()
    # test_slot_book.select_specalization("Cardiologist")
    # time.sleep(1)
    #
    # test_login.login("doctor1@gmail.com", "Doctor@123")
    # time.sleep(1)
    # appointments_table = AppointmentsDB()
    # time.sleep(1)
    # before_status = appointments_table.get_status()
    # test_prescription = TestDoctorPage(driver)
    # test_prescription.navigate_to_url()
    # test_prescription.click_on_view()
    # test_prescription.prescribe()
    # after_status = appointments_table.get_status()
    #
    # assert before_status == "scheduled"
    # assert after_status == "completed"



