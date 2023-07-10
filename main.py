from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        license_plate="พร 4527", 
        height=170)
]

@app.get("/api/test/users")
async def fetch_users():
    return db;

@app.post("/api/test/users")
async def lastest_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.put("/api/test/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.license_plate is not None:
                user.license_plate = user_update.license_plate
            if user_update.height is not None:
                user.height = user_update.height
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does exit"
    )

@app.delete("/api/test/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does exit"
    )
