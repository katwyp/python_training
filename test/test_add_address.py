# -*- coding: utf-8 -*-
from model.address import Address
from test.test_db_matches_ui import test_address_list


def test_add_address(app, db, json_addresses, check_ui):
    address = json_addresses
    old_addresses = db.get_address_list()
    app.address.add_new(address)
    new_addresses = db.get_address_list()
    old_addresses.append(address)
    old = sorted(old_addresses, key=Address.id_or_max)
    new = sorted(new_addresses, key=Address.id_or_max)
    assert old == new
    if check_ui:
        test_address_list(app, db)
