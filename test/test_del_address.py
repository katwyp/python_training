# -*- coding: utf-8 -*-
from model.address import Address


def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    app.address.delete_first()
