from pydantic import BaseModel, Field
from typing import Optional, List, Union
from bson import ObjectId


class Answer(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    question_id: ObjectId
    answer_value: Optional[Union[str, List[str]]]
    survey: ObjectId

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @root_validator(pre=True)
    def validate_answer(cls, values):
        answer_value = values.get('answer_value')

        if isinstance(answer_value, list) and not all(isinstance(item, str) for item in answer_value):
            raise ValueError('All items in answer_value list must be strings.')

        return values
