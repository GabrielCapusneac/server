from fastapi import APIRouter,HTTPException
from storage import fake_db

messages_route=APIRouter()

@messages_route.get("/api/messages")
def get_all_messages():
    discussions = fake_db.get("discussions", {}).values()
    return list(discussions)