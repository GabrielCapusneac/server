from typing import Union
from users.users import users_router
from contacts.contacts import contacts_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(users_router)
app.include_router(contacts_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)