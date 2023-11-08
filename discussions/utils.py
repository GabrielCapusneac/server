import json
from storage.fake_db import fake_db
from uuid import uuid4
from contacts import contacts


# from model import Discussions
# from discussions.discussions


def get_contact_discussion(contacts):
    discussion_data = fake_db.get("discussions", {}).values()
    for discussion in discussion_data:
        if sorted(discussion["contacts"]) == sorted(list(contacts)):
            return True
    return False


# [c1 c2] == [c2 c1]
# sorted([c1 c2]) == sorted([c2 c1])
# [c1 c2 ] == [c1 c2]


# if discussion
# discussion_id = str(uuid4())
# contacts = discussion.get("contacts")
# name =  discussion.get("name")


def create_new_discussion(contacts):
    discussion_data = fake_db.get("discussions", {})
    discussion_id = str(uuid4())
    # discussion_data = data.model_dump()
    # discussion_data["id"] = discussion_content

    discussion_content = {
        "id": discussion_id,
        "contacts": contacts,
        "name": "null"
    }
    discussion_data[discussion_id] = discussion_content

    with open("D:\\server\\storage\\discussions.json", "w") as file:
        json.dump(discussion_data, file, default=str)
    return discussion_content


def remove_duplicate_contacts(contacts):
    return list(dict.fromkeys(contacts))
