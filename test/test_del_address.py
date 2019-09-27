# -*- coding: utf-8 -*-


def test_delete_first_address(app):
    app.session.login(username="admin", password="secret")
    app.address.delete_first()
    app.session.logout()
