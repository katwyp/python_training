# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="added", header="added", footer="added"))
    app.group.edit_first(Group(name="edited"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="added", header="added", footer="added"))
    app.group.edit_first(Group(header="edited"))
