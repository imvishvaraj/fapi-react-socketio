from fastapi import FastAPI
from users_view import user
from database import session_local
app = FastAPI()

app.include_router(user)



@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI Home!"}

