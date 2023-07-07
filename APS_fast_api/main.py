from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        license_plate="กก2893", 
        height=190)
]


@app.get("/api/test/users")
async def fetch_users():
    return db;