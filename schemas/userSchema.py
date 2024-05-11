from typing import Optional
from pydantic import BaseModel, Field, EmailStr


# User Auth
class UserLogin(BaseModel):
    username: str = Field(..., unique=True, description="user username")
    email: EmailStr = Field(..., unique=True, description="User email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


# Update User
class UserRegister(BaseModel):
    username: str = Field(..., unique=True, description="user username")
    email: EmailStr = Field(..., unique=True, description="User email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class ResponseModel(BaseModel):
    message: str
    token: str
