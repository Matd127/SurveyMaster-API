from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List, Union
from bson import ObjectId


class Answer(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')
    question_id: ObjectId
    answer_value: Optional[Union[str, List[str]]]

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
