from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "name"
    textboox_email_id = "email"
    textbox_phone_id = "phone"
    textbox_address_id = "textarea"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.textboox_email_id).clear()
        self.driver.find_element(By.ID, self.textboox_email_id).send_keys(email)

    def setPhone(self,phone):
        self.driver.find_element(By.ID, self.textbox_phone_id).clear()
        self.driver.find_element(By.ID,self.textbox_phone_id).send_keys(phone)

    def setAddress(self,address):
        self.driver.find_element(By.ID,self.textbox_address_id).clear()
        self.driver.find_element(By.ID, self.textbox_address_id).send_keys(address)


