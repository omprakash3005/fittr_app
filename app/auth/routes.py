from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.service import (
    create_access_token, get_current_user_with_roles,
    hash_password, verify_password
)
from app.user.service import create_user_function, get_user_by_email_function
from app.auth.models import UserRegister, UserResponse
from app.user.models import UserCreate
from models import User

router = APIRouter()

@router.post("/register")
def register_user(user: UserRegister):
    # Validate that password and confirm password match
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Password and Confirm Password do not match")

    # Hash the user's password
    hashed_password = hash_password(user.password)

    # Create a User instance using the User model
    new_user = User(
        name=user.name,
        email=user.email,
        gender=user.gender,
        height=user.height,
        weight=user.weight,
        diet_type=user.diet_type,
        password=hashed_password,
        role=user.role
    )

    # Call the function to create the user
    create_user_function(new_user)

    # Return None if the user was created successfully
    return {"message": "User Register successfully"}

@router.post("/login", response_model=UserResponse)
def login_user(creds: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_email_function(creds.username)
    
    if not user or not verify_password(creds.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": user.email})

    return {
        "name": user.name,
        "email": user.email,
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UserResponse)
def get_me(user: UserCreate = Depends(get_current_user_with_roles(["user", "admin"]))):
    return {"name": user.name, "email": user.email}

