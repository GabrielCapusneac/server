from fastapi import APIRouter,HTTPException
from discussions.model import Discussions
from storage import fake_db
from discussions.utils import remove_duplicate_contacs

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

    contacts = remove_duplicate_contacts(contacts)
    contact_discussion = get_contact_discussion(contacts)
    if contact_discussion:
        raise HTTPException(status_code=404, detail="Discussion Already Exists!")

    contacts_discussion = create_new_discussion(contacts)
    return contacts_discussion