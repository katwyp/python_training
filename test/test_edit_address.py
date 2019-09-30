# -*- coding: utf-8 -*-
from model.address import Address


def test_edit_first_address_firstname(app):
    if app.address.count() == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    app.address.edit_first(Address(firstname="edited"))


def test_edit_first_address_company(app):
    if app.address.count() == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    app.address.edit_first(Address(company="edited"))
