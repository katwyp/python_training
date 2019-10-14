# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.address import Address


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = "+" + "(" + ")" + " " + string.digits
    return "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


def random_email(maxlen):
    symbols = "_" + "." + string.digits + string.ascii_letters
    return "".join([random.choice(symbols) for i in range (random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(string.ascii_lowercase) for i in range (random.randrange(maxlen))]) + ".pl"


testdata = [Address(firstname="", lastname="", address="", homephone="", mobile="", workphone="", secondaryphone="",
                    email="", email2="", email3="")] + [
    Address(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 15),
            address=random_string("address", 30),
            homephone=random_number(14), mobile=random_number(14), workphone=random_number(14),
            secondaryphone=random_number(14),
            email=random_email(10), email2=random_email(10), email3=random_email(10))
    for i in range(5)
]


@pytest.mark.parametrized("address", testdata, ids=[repr(x) for x in testdata])
def test_add_address(app, address):
    old_addresses = app.address.get_address_list()
    app.address.add_new(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    old = sorted(old_addresses, key=Address.id_or_max)
    new = sorted(new_addresses, key=Address.id_or_max)
    assert old == new
