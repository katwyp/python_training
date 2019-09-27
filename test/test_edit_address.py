# -*- coding: utf-8 -*-
from model.address import Address


def test_edit_first_address_firstname(app):
    app.address.edit_first(Address(firstname="edited"))


def test_edit_first_address_company(app):
    app.address.edit_first(Address(company="edited"))
