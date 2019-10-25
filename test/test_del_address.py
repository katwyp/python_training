# -*- coding: utf-8 -*-
from model.address import Address
from test.test_db_matches_ui import test_address_list
import random


def test_delete_some_address(app, db, check_ui):
    if len(db.get_address_list()) == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added",
                                    mobile="added", email="added"))
    old_addresses = db.get_address_list()
    address = random.choice(old_addresses)
    app.address.delete_by_id(address.id)
    new_addresses = db.get_address_list()
    assert len(old_addresses) - 1 == len(new_addresses)
    old_addresses.remove(address)
    assert old_addresses == new_addresses
    if check_ui:
        test_address_list(app, db)
