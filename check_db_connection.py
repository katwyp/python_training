from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list = db.get_addresses_not_in_group(Group(id="114"))
    for i in list:
        print(i)
    print(len(list))
finally:
    pass  # db.destroy()
