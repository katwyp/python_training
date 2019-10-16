# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app, json_address):
    address = json_address
    old_addresses = app.address.get_address_list()
    app.address.add_new(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    old = sorted(old_addresses, key=Address.id_or_max)
    new = sorted(new_addresses, key=Address.id_or_max)
    assert old == new
