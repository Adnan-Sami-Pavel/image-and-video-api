
from fastapi import FastAPI, HTTPException, status


app = FastAPI() # type: ignore

textPost: list[str] = ["This is my first post", "This is my second post", "This is my third post"]

allPosts: dict[int, dict[str, str]] = {1: {"title": "First Post", "content": "This is the content of the first post"},
                                       2: {"title": "Second Post", "content": "This is the content of the second post"},
                                       3: {"title": "Third Post", "content": "This is the content of the third post"}}

@app.get("/name") # type: ignore
def my_name() -> dict[str, int | str]:
    return {
        "name": "Adnan Sami Pavel", 
            "age": 27, 
            "country": "Bangladesh"
            } 

@app.get("/about") # type: ignore
def about_me() -> dict[str, int | str | list[str]]:
    return {"name": "Adnan Sami Pavel", "age": 27, "country": "Bangladesh", "hobbies": ["coding", "traveling", "cooking"]}

@app.get("/posts") # type: ignore
def my_posts() -> dict[str, list[str]]:
    return {"posts": textPost }

@app.post("/post-text") # type: ignore
def post_text() -> list[str]:
    textPost[1] = "These are the text that I want to post"
    return textPost

@app.get("/posts/{post_id}") # type: ignore
def get_post(post_id: int) -> dict[str, str]:
    if post_id not in allPosts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post id: {post_id} not found") # type: ignore
    return allPosts[post_id] # type: ignore