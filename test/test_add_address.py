# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app):
    app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
