from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from bson import ObjectId
import re


class User(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    username: str = Field(None, min_length=3, max_length=10)
    email: EmailStr
    password: str = Field(None, min_length=8, max_length=50)

    @field_validator('username')
    def username_alphanumeric(cls, v):
        if not re.match(r'^\w+$', v):
            raise ValueError(
                'must contain only letters, numbers, and underscores')
        return v

    @field_validator('password')
    def password_complexity(cls, v):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$', v):
            raise ValueError(
                'Password must be at least 8 characters long, and include at least one lowercase letter, one uppercase letter, one digit, and one special character')
        return v

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
