from random import randrange
from model.group import Group
from model.address import Address
from fixture.orm import ORMFixture


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_random_address_to_random_group(app, db):
    if len(db.get_address_list()) == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    address = random.choice(db.get_address_list())
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="added", header="added", footer="added"))
    group = random.choice(db.get_group_list())
    old_addresses_in_group = orm.get_addresses_in_group(group)
    app.address.add_address_to_group(address.id, group.id)
    new_addresses_in_group = orm.get_addresses_in_group(group)
    old_addresses_in_group.append(address)
    assert sorted(old_addresses_in_group, key=Address.id_or_max) == sorted(new_addresses_in_group, key=Address.id_or_max)


def test_delete_random_address_from_random_group(app, db):
    if len(db.get_address_list()) == 0:
        app.address.add_new(Address(firstname="added", lastname="added", company="added", address="added", mobile="added", email="added"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="added", header="added", footer="added"))
    group = random.choice(db.get_group_list())
    if len(orm.get_addresses_in_group(group)) == 0:
        address = random.choice(db.get_address_list())
        app.address.add_address_to_group(address.id, group.id)
    old_addresses_in_group = orm.get_addresses_in_group(group)
    address = random.choice(old_addresses_in_group)
    # usuń przypisanie kontaktu do grupy
    new_addresses_in_group = orm.get_addresses_in_group(group)
    old_addresses_in_group.remove(address)
    assert sorted(old_addresses_in_group, key=Address.id_or_max) == sorted(new_addresses_in_group, key=Address.id_or_max)
