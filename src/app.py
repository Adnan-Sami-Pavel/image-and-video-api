from fastapi import FastAPI, HTTPException, status
from typing import List, Dict, Optional, Any, Union, Tuple, Set
from .schema import PostModel, CreatePost, ResponsePost, UpdateModel

app = FastAPI()

all_posts: dict[int, dict[str, Any]] = {
    1: {"title": "FastAPI Basics", "category": "tech", "published": True, "views": 100},
    2: {"title": "Deep Dive into RAG", "category": "ai", "published": True, "views": 500},
    3: {"title": "Privacy Law 101", "category": "legal", "published": False, "views": 20},
    4: {"title": "LLM Agents in Finance", "category": "ai", "published": True, "views": 1000},
    5: {"title": "Contract Analysis Bot", "category": "legal", "published": True, "views": 50},
}


@app.get("/posts")
def get_posts() -> dict[int, dict[str, Any]]:
    return all_posts

@app.get("/posts/status")
def get_published_posts( is_published: bool) -> dict[int, dict[str, Any]]:
    return {
        k: v 
        for k, v in all_posts.items() 
        if v["published"] == is_published
        }

@app.get("/posts/trending")
def get_trending_posts(min_views: int) -> dict[int, dict[str, Any]]:
    return {
        k: v 
        for k, v in all_posts.items() 
        if v["views"] > min_views and v["published"]
        }

@app.get("/search")
def search_posts(query: Optional[str] = None, category: Optional[str] = None, show_drafts: bool = True) -> dict[int, dict[str, Any]]:
    
    available_posts = all_posts.copy()
    
    if category:
        available_posts = {k: v for k, v in all_posts.items() if v["category"] == category.lower()}
    
    if query:
        available_posts = {k: v for k, v in available_posts.items() if query.lower() in v["title"].lower()}
    
    if not show_drafts:
        available_posts = {
            k: v for k, v in available_posts.items()
            if v["published"]
        }
    
    return available_posts



@app.post("/upload_post", response_model= ResponsePost)
def create_post(post: CreatePost):
    post_id = max(all_posts.keys(), default = 0)+1
    response = ResponsePost(
        id = post_id,
        **post.model_dump()
    )
    ##new_post = {"id": post_id, **post.model_dump()}
    all_posts[post_id] = response.model_dump()
    return response
    
@app.put("/edit_post/{post_id}", response_model= ResponsePost)
def update_post(post_id: int, post: CreatePost):
    if post_id not in all_posts:
        raise HTTPException(status_code=404, detail=f"Post {post_id} not found")
    
    response = ResponsePost(
        id = post_id,
        **post.model_dump()
    )
    
    all_posts[post_id] = response.model_dump()
    
    return response

@app.patch("/optional_edit/{post_id}", response_model= ResponsePost)
def optional_edit(post_id: int, post: UpdateModel):
    if post_id not in all_posts:
        raise HTTPException(status_code=404, detail=f"post id {post_id} not found")
    
    ##stored_posts = all_posts[post_id]
    update_contents = post.model_dump(exclude_unset= True)
    
    """updated_post = {**stored_posts, **update_contents}
    all_posts[post_id] = updated_post"""
    
    all_posts[post_id].update(update_contents)
    
    return ResponsePost(**all_posts[post_id])

@app.delete("/post/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int) -> None:
    if post_id not in all_posts:
        raise HTTPException(status_code=404, detail=f"Post id {post_id} not found")
    del all_posts[post_id]
    return None