from pydantic import BaseModel, EmailStr, constr, field_validator, Field
from typing import Optional
from bson import ObjectId
import re


class Tag(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    name: constr(min_length=3, max_length=50)

    @field_validator('name')
    def name_alphanumeric(cls, v):
        if not re.match(r'^\w+$', v):
            raise ValueError(
                'must contain only letters, numbers, and underscores')
        return v

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
