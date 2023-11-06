from fastapi import APIRouter,HTTPException
from discussions.model import Discussions
from storage import fake_db
from discussions.utils import remove_duplicate_contacs, get_contact_discussion, create_new_discussion

discussions_router = APIRouter()

# Id:
# contact: [id1, id2]

@discussions_router.post("/api/discussions")
def create_discussions(discussions_data: Discussions):
    contacts = discussions_data.contacts
    # return list(discussions)

# @discussions_router.get(f"/api/discussions/{discussions_id}")
    users = fake_db.get("users", {})

    for contact in contacts:
        if users.get(str(contact)) is None:
            raise HTTPException(status_code=404, detail="Contact not found")

    contacts = remove_duplicate_contacs(contacts)
    contact_discussion = get_contact_discussion(contacts)
    if contact_discussion:
        raise HTTPException(status_code=404, detail="Discussion Already Exists!")

    contacts_discussion = create_new_discussion(contacts)
    return contacts_discussion

@discussions_router.get("/api/discussions/{user_id}")
def get_discussion(user_id):
    users = fake_db.get("users", {})
    discussions = fake_db.get("discussions", {}).values()
    user_discussions = []
    for discussion in discussions:
        if user_id in discussion["contacts"]:
            for contact in discussion["contacts"]:
                if user_id != contact:
                    discussion["name"] = users[contact].get("name")
                elif len(discussion["contacts"]) == 1:
                    discussion["name"] = users[user_id].get("name")
            user_discussions.append(discussion)
    return user_discussions
