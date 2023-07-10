from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    license_plate: str
    height: int

class UserUpdateRequest(BaseModel):
    license_plate: str
    height: int