from pydantic import BaseModel

class PostModel(BaseModel):
    title: str
    category: str
    published: bool
    views: int
    