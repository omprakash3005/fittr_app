from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
from db import engine
from models import User, Role, UsersRoles
from typing import Optional


def create_user_function(user):
    with Session(engine) as session:
        try:
            new_user = User(
                name=user.name,
                email=user.email,
                gender=user.gender,
                height=user.height,
                weight=user.weight,
                diet_type=user.diet_type,
                password=user.password,
                role=user.role
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

            # Assign the default role 'user'
            user_role = session.exec(select(Role).where(Role.role_name == "user")).first()
            if not user_role:
                session.rollback()
                return {"error": "Default role 'user' not found"}

            # Create a new UsersRoles entry linking the new user to the 'user' role
            user_role_link = UsersRoles(user_id=new_user.user_id, role_id=user_role.role_id)
            session.add(user_role_link)
            session.commit()

            return new_user

        except IntegrityError as e:
            session.rollback()
            return {"error": str(e.orig)}


def update_user_function(user_id: int, user: Optional[User]):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            return {"error": "User not found"}
        try:
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
        except Exception as e:
            session.rollback()
            return {"error": f"An error occurred: {e}"}


def delete_user_function(user_id: int):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            return {"error": "User not found"}
        try:
            session.delete(db_user)
            session.commit()
            return {"message": "User deleted successfully"}
        except Exception as e:
            session.rollback()
            return {"error": f"An error occurred: {e}"}


def get_user_function(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            return user
        return {"error": "User not found"}


def get_all_users_function():
    with Session(engine) as session:
        users = session.query(User).all()
        return users


def get_user_by_email_function(email: str) -> Optional[User]:
    with Session(engine) as session:
        user = session.query(User).filter(User.email == email).first()
        return user
