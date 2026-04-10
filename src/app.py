from fastapi import FastAPI, HTTPException, status
from typing import List, Dict, Optional, Any, Union, Tuple, Set
from .schema import PostModel

app = FastAPI()

all_posts: dict[int, dict[str, Any]] = {
    1: {"title": "FastAPI Basics", "category": "tech", "published": True, "views": 100},
    2: {"title": "Deep Dive into RAG", "category": "ai", "published": True, "views": 500},
    3: {"title": "Privacy Law 101", "category": "legal", "published": False, "views": 20},
    4: {"title": "LLM Agents in Finance", "category": "ai", "published": True, "views": 1000},
    5: {"title": "Contract Analysis Bot", "category": "legal", "published": True, "views": 50},
}



@app.get("/posts")
def get_posts(category: Optional[str] = None, limit: Optional[int] = None) -> dict[int, dict[str, Any]]:
    
    
    if category in {v["category"] for v in all_posts.values()}:
        filtered_posts = {
            k: v 
            for k, v in all_posts.items() 
            if v["category"] == category.lower()
            }
    else:
        filtered_posts = all_posts.copy()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{category} is not a valid category. Valid categories are 'tech', 'ai', and 'legal'.")
        
    
    if limit is not None:
        limited_posts = dict(list(filtered_posts.items())[:limit])
        return limited_posts
    return filtered_posts

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



@app.post("/upload_post", response_model= PostResponse)
def create_post(post: PostModel) -> dict:
    post_id = max(all_posts.keys(), default = 0)+1
    new_post = {"id": post_id, **post.model_dump()}
    all_posts[post_id] = new_post
    return new_post
    

        