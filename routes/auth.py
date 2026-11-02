from fastapi import APIRouter, Depends, HTTPException
from database import db
from schemas import UserSignup, UserLogin
from utils.security import create_access_token, get_current_user, hash_password, verify_password
router = APIRouter()

@router.post("/signup")
async def signup(user:UserSignup):
    existing = await db.user.find_unique(where={"email":user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email Already Registered")
    hash = hash_password(user.password)
    new_user = await db.user.create(data={"email": user.email, "password": hash, "Fullname": user.Fullname})
    return {
        "message": "User Created Succesfully",
        "data": {"id": new_user.id, "email": new_user.email, "Fullname": new_user.Fullname}
    }
@router.post("/login")
async def login(user: UserLogin):
    existing = await db.user.find_unique(where={"email":user.email})
    if not existing:
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    is_password_correct = verify_password (user.password, existing.password)
    if not is_password_correct:
        raise HTTPException(status_code=400, detail= "Invalid credentials")
    access_token = create_access_token({"sub": str(existing.id)})
    return{
        "access_token" : access_token,
        "token_type": "Bearer"
    }

@router.get("/me")
async def get_current_user(user_id=Depends(get_current_user)):
    user = await db.user.find_unique(where={"id": user_id})
    return { "data": { "id": user.id, "email": user.email } }
