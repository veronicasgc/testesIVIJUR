from fastapi import FastAPI, HTTPException
from app.models import User
from typing import Dict

app = FastAPI()

users_db: Dict[int, User] = {}

@app.post("/create-user")
async def create_user(user: User):
    user_id = len(users_db) + 1
    users_db[user_id] = user
    return {"user_id": user_id, "username": user.username, "email": user.email}

@app.get("/get-user/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]
