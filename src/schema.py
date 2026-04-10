from pydantic import BaseModel
from typing import Optional
class PostModel(BaseModel):
    title: str
    category: str
    published: bool
    views: int

class CreatePost(PostModel):
    pass

class ResponsePost(PostModel):
    id: int

class UpdateModel(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    published: Optional[bool] = None
    views: Optional[int] = None