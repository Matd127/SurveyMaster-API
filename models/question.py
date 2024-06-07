from pydantic import BaseModel, constr, Field, model_validator
from typing import Optional
from bson import ObjectId
import re

class Question(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    question_name: constr(min_length=5, max_length=200)
    question_type: constr(regex='^(single|multiple|text)$')
    question_option: Optional[str]
    question_options: Optional[list[str]]
    survey: ObjectId

    @model_validator(pre=True)
    def check_options(cls, values):
        question_type = values.get('question_type')

        if question_type in {'single', 'multiple'} and not values.get('question_options'):
            raise ValueError(
                'Questions of type "single" or "multiple" must have question_options.')

        if question_type == 'text' and values.get('question_options'):
            raise ValueError(
                'Questions of type "text" should not have question_options.')

        if question_type == 'text' and not values.get('question_option'):
            raise ValueError(
                'Questions of type "text" must have a question_option.')

        if question_type in {'single', 'multiple'} and values.get('question_option'):
            raise ValueError(
                'Questions of type "single" or "multiple" should not have question_option.')

        return values

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
