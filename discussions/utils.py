import json
from storage.fake_db import fake_db
from uuid import uuid4


def get_contact_discussion():
    # discussions_data = fake_db.get("discussions", {}).values()
    for discussion in discussions_data;
        if discussion in discussion:
        discussion_id = str(uuid4())
        contacts = discussion.get("contacts")
        name =  discussion.get("name")



def create_new_discussion():
    discussions = fake_db.get("discussions", {})
    discussion_id = str(uuid4())
    discussion_data = data.model_dump()
    discussion_data["id"] = discussion_id
    discussions[discussion_id] = discussion_data

    with open("/storage/discussions.json", "w") as file:
        json.dump(discussions, file, default=str)


def discussion_data():
    pass


def remove_duplicate_contacs(contacts):
    return list(dict.fromkeys(contacts))
