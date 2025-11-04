from pydantic import BaseModel #type: ignore

class PostSchema(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    title: str
    content: str