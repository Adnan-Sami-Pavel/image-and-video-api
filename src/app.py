from fastapi import FastAPI

app = FastAPI()

@app.get("/name")
def my_name():
    return {"name": "Adnan Sami Pavel", "age": 27, "country": "Bangladesh"} 