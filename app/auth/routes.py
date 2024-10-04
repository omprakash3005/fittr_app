from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlmodel import select, Session
from app.auth.service import (
    create_access_token, get_current_user_with_roles,
    hash_password, verify_password
)
from app.user.service import create_user_function, get_user_by_email_function
from app.auth.models import UserRegister, UserResponse
from app.user.models import UserCreate
from models import User, Role, UsersRoles
from db import engine

router = APIRouter()

@router.post("/register")
def register_user(user: UserRegister):
    with Session(engine) as session:
        try:
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

            # Add the new user to the database
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

            # Query the Role table to get the corresponding role_id based on the role_name
            user_role = session.exec(select(Role).where(Role.role_name == user.role)).first()

            # Check if the role exists in the Role table
            if not user_role:
                session.rollback()
                raise HTTPException(status_code=404, detail=f"Role '{user.role}' not found")

            # Create a new UsersRoles entry linking the new user to the role
            user_role_link = UsersRoles(user_id=new_user.user_id, role_id=user_role.role_id)
            session.add(user_role_link)
            session.commit()

            return {"message": "User registered successfully"}

        except IntegrityError as e:
            session.rollback()
            raise HTTPException(status_code=400, detail=f"Integrity error: {str(e.orig)}")


@router.post("/login", response_model=UserResponse)
def login_user(creds: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        # Retrieve the user by email (username field in OAuth2PasswordRequestForm represents email)
        user = get_user_by_email_function(creds.username)
        
        # Verify the user's password
        if not user or not verify_password(creds.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        
        # Generate an access token
        access_token = create_access_token({"sub": user.email})

        # Return the user information along with the access token
        return {
            "name": user.name,
            "email": user.email,
            "access_token": access_token,
            "token_type": "bearer"
        }

@router.get("/me", response_model=UserResponse)
def get_me(user: UserCreate = Depends(get_current_user_with_roles(["user", "admin"]))):
    return {"name": user.name, "email": user.email}
