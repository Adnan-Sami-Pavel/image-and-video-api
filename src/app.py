from fastapi import FastAPI

app = FastAPI()

textPost = ["This is my first post", "This is my second post", "This is my third post"]

@app.get("/name")
def my_name():
    return {"name": "Adnan Sami Pavel", "age": 27, "country": "Bangladesh"} 

@app.get("/about")
def about_me():
    return {"name": "Adnan Sami Pavel", "age": 27, "country": "Bangladesh", "hobbies": ["coding", "traveling", "cooking"]}

@app.get("/posts")
def my_posts():
    return {"posts": textPost }

@app.post("/post-text")
def post_text():
    textPost[1] = "These are the text that I want to post"
    return textPost