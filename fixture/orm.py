from pony.orm import *
from datetime import datetime
from model.group import Group
from model.address import Address


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        addresses = Set(lambda: ORMFixture.ORMAddress, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMAddress(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="addresses", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_addresses_to_model(self, addresses):
        def convert(address):
            return Address(id=str(address.id), firstname=address.firstname, lastname=address.lastname)
        return list(map(convert, addresses))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_address_list(self):
        return self.convert_addresses_to_model(select(a for a in ORMFixture.ORMAddress if a.deprecated is None))

    @db_session
    def get_addresses_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_addresses_to_model(orm_group.addresses)

    @db_session
    def get_addresses_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_addresses_to_model(select(a for a in ORMFixture.ORMAddress if a.deprecated is None and orm_group not in a.groups))