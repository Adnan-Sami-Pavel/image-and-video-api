from pydantic import BaseModel

class PostModel(BaseModel):
    title: str
    category: str
    published: bool
    views: int

class CreatePost(PostModel):
    pass

class ResponsePost(PostModel):
    id: int