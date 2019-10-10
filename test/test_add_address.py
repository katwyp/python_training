# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app):
    old_addresses = app.address.get_address_list()
    address = Address(firstname="new3", lastname="new3", address="new 4, 777777 new",
                      homephone="123556789", mobile="600808600", workphone="293394467", secondaryphone="097767432",
                      email="neeew@new.pl", email2="neeew2@new2.pl", email3="neeew3@new3.pl")
    app.address.add_new(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    old = sorted(old_addresses, key=Address.id_or_max)
    new = sorted(new_addresses, key=Address.id_or_max)
    assert old == new


# def test_add_address_second(app):
#    old_addresses = app.address.get_address_list()
#    address = Address(firstname="second", lastname="second")
#    app.address.add_new(address)
#    new_addresses = app.address.get_address_list()
#    assert len(old_addresses) + 1 == len(new_addresses)
#    old_addresses.append(address)
#    old = sorted(old_addresses, key=Address.id_or_max)
#    new = sorted(new_addresses, key=Address.id_or_max)
#    assert old == new


# def test_add_address_third(app):
#    old_addresses = app.address.get_address_list()
#    address = Address(firstname="third", lastname="third")
#    app.address.add_new(address)
#    new_addresses = app.address.get_address_list()
#    assert len(old_addresses) + 1 == len(new_addresses)
#    old_addresses.append(address)
#    old = sorted(old_addresses, key=Address.id_or_max)
#    new = sorted(new_addresses, key=Address.id_or_max)
#    assert old == new
