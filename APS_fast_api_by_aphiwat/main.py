from typing import List
from uuid import UUID,uuid4
from fastapi import FastAPI
from models import User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        license_plate="กก2893", 
        height=190),
    User(
        id=uuid4(), 
        license_plate="กก2894", 
        height=180)
]

# http://127.0.0.1:8000/api/test2/user?lp=%E0%B8%81%E0%B8%941235&height=200
# @app.get("/api/test2/user")
# async def data(lp:str,height:int):
#     return {"Licenes_Plate": lp, "Height": height}


@app.get("/api/test/users")
async def fetch_users():
    return db;

@app.post("/api/test/users")
async def lastest_user(user: User):
    db.append(user)
    return {"id": user.id}
