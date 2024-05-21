import time
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass


class TestAdminPage:

    def __init__(self, driver):
        self.driver = driver

    def click_doctor_view(self):
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'doctor-view-btn'))
        print("2 .Entered Doctors Index Path")

    def click_medicine_view(self):
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, '//a[text()="Manage Medicines"]'))
        print("2 .Entered Medicine Index Path")

    def add_doctor(self, name, email, phone, yoe, fee, sid):
        self.driver.get("http://localhost:3000/doctors")
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'myInput'))
        print("3. Click on Add Button")
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'name'), name)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'email'), email)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'phone_number'), phone)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'years_of_experiance'), yoe)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'consultation_fee'), fee)
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'specialization_id'))
        BaseClass(self.driver, 3).wait_and_click((By.XPATH, f'//select[@id="specialization_id"]//option[@value="{sid}"]'))
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'doc-submit-btn'))
        print(f"DOCTOR ADDED SUCCESFULLY-{name}")
        time.sleep(1)

    def add_medicine(self, image, name, description, price, dosage, quantity, pid):
        self.driver.get("http://localhost:3000/medicines")
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'myInput'))
        print("3. Click on Add Button")
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'medicine_picture'), image)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'name'), name)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'description'), description)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'price'), price)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'dosage'), dosage)
        BaseClass(self.driver, 3).wait_and_send_keys((By.ID, 'quantity'), quantity)
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'need_prescription'))
        BaseClass(self.driver, 3).wait_and_click(
            (By.XPATH, f'//select[@id="need_prescription"]//option[@value="{pid}"]'))
        BaseClass(self.driver, 3).wait_and_click((By.ID, 'med-submit-btn'))
        time.sleep(1)
        print(f"MEDICINE ADDED SUCCESFULLY-{name}")
