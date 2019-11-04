import re
from random import randrange
from model.group import Group
from model.address import Address


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_address_list(app, db):
    ui_list = app.address.get_address_list()
    db_list = map(clean, db.get_address_list())
    assert sorted(ui_list, key=Address.id_or_max) == sorted(db_list, key=Address.id_or_max)


def test_all_addresses_on_home_page(app, db):
    address_list_from_ui = sorted(app.address.get_address_list(), key=Address.id_or_max)
    address_list_from_db = sorted(db.get_address_list(), key=Address.id_or_max)
    index = 0
    for address in db.get_address_list():
        address_from_home_page = address_list_from_ui[index]
        address_from_db = address_list_from_db[index]
        assert address_from_home_page.firstname == clear_string(address_from_db.firstname).strip()
        assert address_from_home_page.lastname == clear_string(address_from_db.lastname).strip()
        assert address_from_home_page.address == clear_string(address_from_db.address).strip()
        assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_db)
        assert address_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(address_from_db)
        index = index + 1


def test_random_address_on_home_page(app, db):
    index = randrange(len(db.get_address_list()))
    address_from_home_page = sorted(app.address.get_address_list(), key=Address.id_or_max)[index]
    address_from_db = sorted(db.get_address_list(), key=Address.id_or_max)[index]
    assert address_from_home_page.firstname == clear_string(address_from_db.firstname).strip()
    assert address_from_home_page.lastname == clear_string(address_from_db.lastname).strip()
    assert address_from_home_page.address == clear_string(address_from_db.address).strip()
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_db)
    assert address_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(address_from_db)


def clear_phone(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [address.homephone, address.mobile, address.workphone,
                                        address.secondaryphone]))))


def merge_emails_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [address.email, address.email2, address.email3])))


def clear_string(s):
    return re.sub("  ", " ", s)


def clean(address):
    return Address(id=address.id, firstname=clear_string(address.firstname).strip(),
                   lastname=clear_string(address.lastname).strip(),
                   address=clear_string(address.address).strip(),
                   all_phones_from_home_page=merge_phones_like_on_home_page(address),
                   all_emails_from_home_page=merge_emails_like_on_home_page(address))
