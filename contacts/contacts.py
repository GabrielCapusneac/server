from fastapi import APIRouter, HTTPException
from storage.fake_db import fake_db
from users.models import UserCreate

contacts_router = APIRouter()


@contacts_router.get("/api/contacts")
def get_all_contacts():
    users = fake_db.get("users", {}).values()
    return list(users)

