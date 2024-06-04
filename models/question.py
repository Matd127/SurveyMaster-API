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


class Question(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    question_name: constr(min_length=5, max_length=200)
    question_option: Optional[str]
    question_options: Optional[list[str]]
    surveys: Optional[list[ObjectId]] = []
