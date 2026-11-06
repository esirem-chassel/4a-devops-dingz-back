from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Show the current API version")
async def home():
    return {"version": "0.1a"}
