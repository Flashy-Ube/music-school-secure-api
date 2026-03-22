#api/auth.py

import os
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv #you need python-dotenv

import ctypes
lib = ctypes.CDLL("./assembly/verify_token.so")

security = HTTPBearer()



load_dotenv() #loads .env variables

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("SECRET_KEY not set")

ALGORITHM = "HS256"

def create_token(user_id, role: str):
    payload = {
            "user_id": user_id,
            "role": role,
            "exp": datetime.utcnow() + timedelta(minutes=30)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
   
    #asm verfication layer
    result = lib.verify_signature(0,0)
    if result != 1:
        raise HTTPException(status_code=401, detail="INVALID token (asm check failed)")



    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {
                "user_id": payload["user_id"],
                "role": payload["role"]
        }
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
