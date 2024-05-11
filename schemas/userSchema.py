from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

# User Auth
class UserAuth(BaseModel):
    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


# Update User
class UserRegister(BaseModel):
    username: str = Field(..., unique=True)
    email: str = Field(..., unique=True)
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None