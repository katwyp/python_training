from sys import maxsize


class Address:

    def __init__(self, firstname=None, lastname=None, company=None, address=None,
                 email=None, email2=None, email3=None,
                 homephone=None, mobile=None, workphone=None, secondaryphone=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id

    def __repr__(self):
        return "%s:%s %s, %s" % (self.id, self.firstname, self.lastname, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
