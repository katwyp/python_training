

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_new_address(self, address):
        wd = self.app.wd
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
