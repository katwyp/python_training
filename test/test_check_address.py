import re
from random import randrange


def test_random_address_on_home_page(app):
    index = randrange(app.address.count())
    address_from_home_page = app.address.get_address_list()[index]
    address_from_edit_page = app.address.get_address_info_from_edit_page(index)
    assert address_from_home_page.firstname == address_from_edit_page.firstname
    assert address_from_home_page.lastname == address_from_edit_page.lastname
    assert address_from_home_page.address == address_from_edit_page.address
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)
    assert address_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(address_from_edit_page)


def test_phones_on_address_view_page(app):
    index = randrange(app.address.count())
    address_from_edit_page = app.address.get_address_info_from_edit_page(index)
    address_from_view_page = app.address.get_address_from_view_page(index)
    assert address_from_edit_page.homephone == address_from_view_page.homephone
    assert address_from_edit_page.workphone == address_from_view_page.workphone
    assert address_from_edit_page.mobile == address_from_view_page.mobile
    assert address_from_edit_page.secondaryphone == address_from_view_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [address.homephone, address.mobile, address.workphone,
                                        address.secondaryphone]))))


def merge_emails_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [address.email, address.email2, address.email3])))
