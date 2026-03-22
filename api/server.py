#api/server.py  

from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from .auth import verify_token, create_token
from .access_control import check_permission

app = FastAPI(title="Secure Music School API")

class LoginRequest(BaseModel):
    username: str
    password: str

#demo login endpoint
@app.post("/login")
def login(data: LoginRequest):
    #in production: fetch from DB and verify password ie fake users (for now)
    demo_users = {
            "alice": {"user_id": 1, "role": "student"}, 
            "bob": {"user_id": 2, "role": "teacher"}, 
            "admin": {"user_id": 3, "role": "admin"}
    }

    user = demo_users.get(data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_token(user["user_id"], user["role"])
    
    return {
            "access_token": token,
            "token_type": "bearer"
    }

#lessons endpoint
@app.get("/lessons")
def get_lessons(user=Depends(verify_token)):
    check_permission(user, "VIEW_LESSONS")


    #in production: fetch lessons from DB fake data
    return {"data": [{"lesson_id": 1, "title": "Piano Basics"}]}
