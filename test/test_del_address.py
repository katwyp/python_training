# -*- coding: utf-8 -*-
from model.address import Address
from random import randrange


def test_delete_some_address(app):
    if app.address.count() == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    old_addresses = app.address.get_address_list()
    index = randrange(len(old_addresses))
    app.address.delete_by_index(index)
    assert len(old_addresses) - 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[index:index+1] = []
    assert old_addresses == new_addresses
