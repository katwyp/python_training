# -*- coding: utf-8 -*-
from model.address import Address


def test_edit_first_address(app):
    app.session.login(username="admin", password="secret")
    app.address.edit_first(Address(firstname="edited", lastname="edited", company="edited", address="edited", mobile="edited", email="edited"))
    app.session.logout()
