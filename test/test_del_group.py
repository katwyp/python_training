from model.group import Group
from test.test_db_matches_ui import test_group_list
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="added", header="added", footer="added"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        test_group_list(app, db)
