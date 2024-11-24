from typing import Optional
from pydantic import BaseModel, EmailStr

class CreateUserRequest(BaseModel):
    """User model for the application to create a new user"""
    username: str
    email: str

class UpdateUserRequest(BaseModel):
    user_id: int
    name: Optional[str] = None
    email: Optional[EmailStr] = None

    @classmethod
    def validate_update(cls, values):
        if not values.get("name") and not values.get("email"):
            raise ValueError("At least one of 'name' or 'email' must be provided.")
        return values