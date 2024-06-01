from pydantic import BaseModel, EmailStr, constr, field_validator, Field
from typing import Optional
from bson import ObjectId
import re


class ObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)


class User(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8, max_length=50)

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
