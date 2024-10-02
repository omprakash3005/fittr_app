from fastapi import APIRouter, HTTPException, Depends
from app.user.service import (
    create_user_function, get_all_users_function, get_user_function, update_user_function, 
    delete_user_function
)
from app.user.models import UserCreate, UserUpdate
from app.auth.service import hash_password

router = APIRouter()

@router.get("/")
def read_root():
    response = get_all_users_function()
    return response

@router.get("/{user_id}")
def read_user(user_id: int):
    response = get_user_function(user_id)
    if response:
        return response
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/")
def create_user(user: UserCreate):
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    response = create_user_function(user)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return {"message": "User created successfully!", "user": response}

@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    response = update_user_function(user_id, user)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return {"message": "User updated successfully!"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    response = delete_user_function(user_id)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return {"message": "User deleted successfully!"}
