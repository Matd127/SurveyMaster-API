from pydantic import BaseModel, field_validator, Field
from typing import Optional
from bson import ObjectId
import re


class Tag(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    name: str = Field(None, min_length=3, max_length=50)

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
