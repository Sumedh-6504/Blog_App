from pydantic import BaseModel #type: ignore
import uuid
from fastapi_users import schemas

class PostSchema(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    title: str
    content: str

class UserCreate(schemas.BaseUserCreate):
    pass

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass