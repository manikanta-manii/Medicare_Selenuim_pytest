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
        base_class = BaseClass(self.driver, 3)
        self.driver.get("http://localhost:3000/doctors")
        base_class.wait_and_click((By.ID, 'myInput'))
        print("3. Click on Add Button")
        base_class.wait_and_send_keys((By.ID, 'name'), name)
        base_class.wait_and_send_keys((By.ID, 'email'), email)
        base_class.wait_and_send_keys((By.ID, 'phone_number'), phone)
        base_class.wait_and_send_keys((By.ID, 'years_of_experiance'), yoe)
        base_class.wait_and_send_keys((By.ID, 'consultation_fee'), fee)
        base_class.wait_and_click((By.ID, 'specialization_id'))
        base_class.wait_and_click((By.XPATH, f'//select[@id="specialization_id"]//option[@value="{sid}"]'))
        base_class.wait_and_click((By.ID, 'doc-submit-btn'))
        print(f"DOCTOR ADDED SUCCESFULLY-{name}")
        time.sleep(1)

    def add_medicine(self, image, name, description, price, dosage, quantity, pid):
        base_class = BaseClass(self.driver, 3)
        self.driver.get("http://localhost:3000/medicines")
        base_class.wait_and_click((By.ID, 'myInput'))
        print("3. Click on Add Button")
        base_class.wait_and_send_keys((By.ID, 'medicine_picture'), image)
        base_class.wait_and_send_keys((By.ID, 'name'), name)
        base_class.wait_and_send_keys((By.ID, 'description'), description)
        base_class.wait_and_send_keys((By.ID, 'price'), price)
        base_class.wait_and_send_keys((By.ID, 'dosage'), dosage)
        base_class.wait_and_send_keys((By.ID, 'quantity'), quantity)
        base_class.wait_and_click((By.ID, 'need_prescription'))
        base_class.wait_and_click(
            (By.XPATH, f'//select[@id="need_prescription"]//option[@value="{pid}"]'))
        base_class.wait_and_click((By.ID, 'med-submit-btn'))
        time.sleep(1)
        print(f"MEDICINE ADDED SUCCESFULLY-{name}")
