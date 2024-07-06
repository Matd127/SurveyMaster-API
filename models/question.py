from pydantic import BaseModel, ConfigDict,  Field
from typing import Optional, List
from bson import ObjectId


class Question(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    question_name: str = Field(None, min_length=5, max_length=200)
    question_type: str = Field(None, pattern='^(single|multiple|text)$')
    question_options: Optional[List[str]]
    survey: ObjectId

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
