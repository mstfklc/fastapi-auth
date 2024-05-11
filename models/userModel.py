from typing import Optional, Required
from beanie import Document
from pydantic import Field, EmailStr


class UserModel(Document):
    user_id: str = Field(..., unique=True)
    username: str = Field(..., unique=True, description="user username")
    email: EmailStr = Field(..., unique=True, description="User email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: bool = Field(default=False)


