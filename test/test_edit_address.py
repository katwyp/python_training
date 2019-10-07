# -*- coding: utf-8 -*-
from model.address import Address


def test_edit_first_address_firstname(app):
    if app.address.count() == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    old_addresses = app.address.get_address_list()
    address = Address(firstname="edited")
    address.id, address.lastname = old_addresses[0].id, old_addresses[0].lastname
    app.address.edit_first(address)
    assert len(old_addresses) == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[0] = address
    old = sorted(old_addresses, key=Address.id_or_max)
    new = sorted(new_addresses, key=Address.id_or_max)
    assert old == new


# def test_edit_first_address_company(app):
#    if app.address.count() == 0:
#        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
#    app.address.edit_first(Address(company="edited"))
