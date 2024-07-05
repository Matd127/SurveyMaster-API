from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId


class Question(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    question_name: str = Field(None, min_length=5, max_length=200)
    question_type: str = Field(None, pattern='^(single|multiple|text)$')
    question_option: Optional[str] = Field(None)
    question_options: Optional[List[str]]
    survey: ObjectId

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
