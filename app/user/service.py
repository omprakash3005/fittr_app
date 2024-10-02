from sqlmodel import Session
from db import engine
from models import User
from typing import Optional

def create_user_function(user):
    with Session(engine) as session:
        try:
            new_user = User(
                name=user.name, email=user.email, gender=user.gender,
                height=user.height, weight=user.weight, diet_type=user.diet_type,
                password=user.password, role=user.role
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return {
                "message": "User created successfully",
                "user_id": new_user.user_id,
                "name": new_user.name,
                "email": new_user.email
            }
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

def update_user_function(user_id: int, user: Optional[User]):
    with Session(engine) as session:
        try:
            db_user = session.get(User, user_id)
            if db_user:
                if user.name:
                    db_user.name = user.name
                if user.email:
                    db_user.email = user.email
                if user.gender:
                    db_user.gender = user.gender
                if user.height:
                    db_user.height = user.height
                if user.weight:
                    db_user.weight = user.weight
                if user.diet_type:
                    db_user.diet_type = user.diet_type
                if user.role:
                    db_user.role = user.role
                session.commit()
                return {"message": "User updated successfully"}
            return {"error": "User not found"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

def delete_user_function(user_id: int):
    with Session(engine) as session:
        try:
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                session.commit()
                return {"message": "User deleted successfully"}
            return {"error": "User not found"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

def get_user_function(user_id: int):
    with Session(engine) as session:
        try:
            user = session.get(User, user_id)
            if user:
                return user
            return {"error": "User not found"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

def get_all_users_function():
    with Session(engine) as session:
        try:
            users = session.query(User).all()
            return users
        except Exception as e:
            return {"error": f"An error occurred: {e}"}
def get_user_by_email_function(email: str) -> User | None:
    with Session(engine) as session:
        user = session.query(User).filter(User.email == email).first()
        return user