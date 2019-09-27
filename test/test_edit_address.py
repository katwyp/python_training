# -*- coding: utf-8 -*-
from model.address import Address


def test_edit_first_address_firstname(app):
    app.session.login(username="admin", password="secret")
    app.address.edit_first(Address(firstname="edited"))
    app.session.logout()

def test_edit_first_address_company(app):
    app.session.login(username="admin", password="secret")
    app.address.edit_first(Address(company="edited"))
    app.session.logout()
