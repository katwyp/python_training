# -*- coding: utf-8 -*-
import pytest
from model.address import Address
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address(app):
    app.session.login(username="admin", password="secret")
    app.address.add_new_address(Address(firstname="rryjyrjryjy", lastname="hryrjry", company="nethethet", address="nethethethet", mobile="fnjntyjte", email="jetjhethjet"))
    app.session.logout()
