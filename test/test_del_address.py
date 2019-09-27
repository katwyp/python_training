# -*- coding: utf-8 -*-


def test_delete_first_address(app):
    app.address.delete_first()
