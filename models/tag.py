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


class Tag(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    name: constr(min_length=3, max_length=50)

    @field_validator('name')
    def name_alphanumeric(cls, v):
        if not re.match(r'^\w+$', v):
            raise ValueError(
                'must contain only letters, numbers, and underscores')
        return v
