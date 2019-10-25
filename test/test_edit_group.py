# -*- coding: utf-8 -*-
from model.group import Group
from test.test_db_matches_ui import test_group_list
import random


def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="added", header="added", footer="added"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="new_edited")
    app.group.edit_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.name = new_group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        test_group_list(app, db)
