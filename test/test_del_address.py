# -*- coding: utf-8 -*-
from model.address import Address


def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    old_addresses = app.address.get_address_list()
    app.address.delete_first()
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) - 1 == len(new_addresses)
    old_addresses[0:1] = []
    assert old_addresses == new_addresses
