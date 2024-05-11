from typing import Optional
from uuid import UUID, uuid4
from beanie import Document
from pydantic import Field


class UserModel(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: str = Field(..., unique=True)
    email: str = Field(..., unique=True)
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: bool = Field(default=False)


