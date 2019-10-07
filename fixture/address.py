from model.address import Address


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
        self.change_field_value("mobile", address.mobile)
        self.change_field_value("email", address.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_by_index(self, index, new_address_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_address_form(new_address_data)
        wd.find_element_by_name("update").click()
        self.address_cache = None

    def edit_first(self):
        self.edit_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
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
                self.address_cache.append(Address(lastname=lastname, firstname=firstname, id=id_address))
        return list(self.address_cache)
