from model.address import Address
import re


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, address):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(address)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.address_cache = None

    def fill_address_form(self, address):
        self.change_field_value("firstname", address.firstname)
        self.change_field_value("lastname", address.lastname)
        self.change_field_value("company", address.company)
        self.change_field_value("address", address.address)
        self.change_field_value("home", address.homephone)
        self.change_field_value("mobile", address.mobile)
        self.change_field_value("work", address.workphone)
        self.change_field_value("phone2", address.secondaryphone)
        self.change_field_value("email", address.email)
        self.change_field_value("email2", address.email2)
        self.change_field_value("email3", address.email3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_by_index(self, index, new_address_data):
        wd = self.app.wd
        self.open_address_to_edit_by_index(index)
        self.fill_address_form(new_address_data)
        wd.find_element_by_name("update").click()
        self.address_cache = None

    def edit_by_id(self, id, new_address_data):
        wd = self.app.wd
        self.open_address_to_edit_by_id(id)
        self.fill_address_form(new_address_data)
        wd.find_element_by_name("update").click()
        self.address_cache = None

    def view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def edit_first(self):
        self.edit_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.address_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//tr[@name='entry']//input[@value='%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.address_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.address_cache = []
            for element in wd.find_elements_by_name("entry"):
                row_elements = element.find_elements_by_tag_name("td")
                id_address = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = row_elements[1].text
                firstname = row_elements[2].text
                address = row_elements[3].text
                all_emails = row_elements[4].text
                all_phones = row_elements[5].text
                self.address_cache.append(Address(lastname=lastname, firstname=firstname, id=id_address,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.address_cache)

    def open_address_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def add_address_to_group(self, address_id, group_id):
        wd = self.app.wd
        self.open_address_to_edit_by_id(address_id)
        # wybrać z listy grupę po id
        wd.find_element_by_name("update").click()
        self.address_cache = None

    def open_address_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//a[contains(@href, 'edit.php?id=%s')]" % id).click()

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_address_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Address(firstname=firstname, lastname=lastname, id=id, address=address,
                       email=email, email2=email2, email3=email3,
                       homephone=homephone, workphone=workphone, mobile=mobile, secondaryphone=secondaryphone)

    def get_address_from_view_page(self, index):
        wd = self.app.wd
        self.view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Address(homephone=homephone, workphone=workphone, mobile=mobile, secondaryphone=secondaryphone)
