# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app):
    app.session.login(username="admin", password="secret")
    app.address.add_new_address(Address(firstname="rryjyrjryjy", lastname="hryrjry", company="nethethet", address="nethethethet", mobile="fnjntyjte", email="jetjhethjet"))
    app.session.logout()
