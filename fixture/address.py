

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, address):
        wd = self.app.wd
        self.app.open_home_page()
        # init address addition
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(address)
        # submit address addition
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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

    def edit_first(self, new_address_data):
        wd = self.app.wd
        self.app.open_home_page()
        # find first address to edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_address_form(new_address_data)
        # submit address update
        wd.find_element_by_name("update").click()

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first address
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))
