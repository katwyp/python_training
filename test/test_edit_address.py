# -*- coding: utf-8 -*-
from model.address import Address
import random
from test.test_db_matches_ui import test_address_list


def test_edit_some_address_firstname(app, db, check_ui):
    if len(db.get_address_list()) == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    old_addresses = db.get_address_list()
    address = random.choice(old_addresses)
    new_address = Address(firstname="edited")
    app.address.edit_by_id(address.id, new_address)
    new_addresses = db.get_address_list()
    assert len(old_addresses) == len(new_addresses)
    address.firstname = new_address.firstname
    old = sorted(old_addresses, key=Address.id_or_max)
    new = sorted(new_addresses, key=Address.id_or_max)
    assert old == new
    if check_ui:
        test_address_list(app, db)
