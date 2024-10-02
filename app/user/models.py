from pydantic import BaseModel, EmailStr
from typing import Optional

# User creation schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    gender: str
    height: float
    weight: float
    diet_type: str
    password: str
    confirm_password: str
    role: Optional[str] = "user"

# User update schema
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    diet_type: Optional[str] = None
    role: Optional[str] = "user"

# User response schema to fetch user details
class UserResponse(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    gender: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    diet_type: Optional[str]
    role: Optional[str]="user"

    class Config:
        from_attributes = True
