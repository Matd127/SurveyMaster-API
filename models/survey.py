from pydantic import BaseModel, constr, field_validator, Field
from typing import Optional
from bson import ObjectId
import re
import datetime


class ObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)


class Survey(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id', default=None)  # Temporary
    title: constr(min_length=3, max_length=50)
    description: constr(min_length=10, max_length=255)
    start_date: datetime.datetime
    end_date: datetime.datetime
    is_open: bool
    owner: constr(min_length=3, max_length=50)  # Temporary
    tags: Optional[list[ObjectId]] = []  # Temporary

    @field_validator('title')
    def title_alphanumeric(cls, v):
        if not re.match(r'^[\w\s.,?!-]+$', v):
            raise ValueError(
                'Title must contain only letters, numbers, spaces, and common punctuation')
        return v
