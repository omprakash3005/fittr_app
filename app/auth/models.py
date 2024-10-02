from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    name: str
    email: str
    gender: str
    height: float
    weight: float
    diet_type: str
    password: str
    confirm_password: str
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    access_token: str | None = None
    token_type: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str
