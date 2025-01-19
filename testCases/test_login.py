import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://testautomationpractice.blogspot.com/"
    username = 'abcd'
    email = 'abcd@gmail.com'
    phone = '1234567890'
    address = """I Plot No 123,
                ERN Road,
                Pin - 444444"""

    def test_homePage(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title =="Automation Testing Practice":
            assert True
        else:
            assert False


    def test_enterDetails(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setEmail(self.email)
        self.lp.setPhone(self.phone)
        self.lp.setAddress(self.address)
        assert True






