from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import ForeignKey

# User model
class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, nullable=False)
    email: str = Field(max_length=255, nullable=False, unique=True)
    gender: str = Field(max_length=10, nullable=False)
    height: float = Field(nullable=False)
    weight: float = Field(nullable=False)
    diet_type: str = Field(max_length=20, nullable=False)
    password: str = Field(max_length=255, nullable=False)
    role: Optional[str] = Field(default="user", max_length=50)

# Role model
class Role(SQLModel, table=True):
    role_id: Optional[int] = Field(default=None, primary_key=True)
    role_name: str = Field(max_length=255, nullable=False)

# UsersRoles model (linking table between Users and Roles)
class UsersRoles(SQLModel, table=True):
    users_roles_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(ForeignKey("user.user_id"), nullable=False)
    role_id: int = Field(ForeignKey("role.role_id"), nullable=False)

# Permissions model (defines permissions for roles)
class Permissions(SQLModel, table=True):
    permission_id: Optional[int] = Field(default=None, primary_key=True)
    permission_name: str = Field(max_length=255, nullable=False)
    role_id: int = Field(ForeignKey("role.role_id"), nullable=False)

# DietPlan model (linking user and dietitian for diet plan)
class DietPlan(SQLModel, table=True):
    __tablename__ = "dietplan"
    __table_args__ = {"extend_existing": True}  # Allow redefinition if already exists
    diet_plan_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(ForeignKey("user.user_id"), nullable=False)
    dietitian_user_id: int = Field(ForeignKey("user.user_id"), nullable=False)  # Links to the dietitian's user ID
    proteins: float = Field(nullable=False)  # Amount of Proteins in grams
    carbs: float = Field(nullable=False)  # Amount of Carbohydrates in grams
    fats: float = Field(nullable=False)  # Amount of Fats in grams
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
    plan_status: Optional[str] = Field(default="active", max_length=20)
