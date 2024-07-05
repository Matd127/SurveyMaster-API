from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from bson import ObjectId
import re
import datetime


class Survey(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    title: str = Field(None, min_length=3, max_length=50)
    description: str = Field(None, min_length=10, max_length=255)
    start_date: datetime
    end_date: datetime
    is_open: bool
    owner: ObjectId
    tags: Optional[List[ObjectId]] = Field(default_factory=list)

    @field_validator('title')
    def title_alphanumeric(cls, v):
        if not re.match(r'^[\w\s.,?!-]+$', v):
            raise ValueError(
                'Title must contain only letters, numbers, spaces, and common punctuation')
        return v

    @field_validator('end_date')
    def check_dates(cls, v, values):
        start_date = values.get('start_date')
        if start_date and v < start_date:
            raise ValueError('End date must be after start date')
        return v

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
