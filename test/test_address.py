from random import randrange


def test_address_on_home_page(app):
    index = randrange(app.address.count())
    address_from_home_page = app.address.get_address_list()[index]
    address_from_edit_page = app.address.get_address_info_from_edit_page(index)
    assert address_from_home_page.address == address_from_edit_page.address
