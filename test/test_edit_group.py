# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="edited"))


def test_edit_first_group_header(app):
    app.group.edit_first(Group(header="edited"))
