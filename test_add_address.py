# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from address import Address


class TestAddAddress(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def add_new_address(self, wd, address):
        # init address addition
        wd.find_element_by_link_text("add new").click()
        # fill address form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(address.lastname)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(address.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.address)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(address.mobile)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(address.email)
        # submit address addition
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_address(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_address(wd, Address(firstname="rryjyrjryjy", lastname="hryrjry", company="nethethet", address="nethethethet", mobile="fnjntyjte", email="jetjhethjet"))
        self.logout(wd)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException:
            return False
        return True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
