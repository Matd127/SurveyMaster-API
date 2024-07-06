import pytest
from pydantic import ValidationError
from bson import ObjectId
from models.question import Question

valid_question_data = {
    "question_name": "Sample question",
    "question_type": "single",
    "question_options": ["Option A", "Option B", "Option C"],
    "survey": ObjectId()
}

invalid_question_data = {
    "question_name": "Short",
    "question_type": "invalid_type",
    "question_options": ["Option A", 123, True],
    "survey": "invalid_object_id"
}

def test_create_question_valid():
    question = Question(**valid_question_data)
    assert question

def test_create_question_invalid():
    with pytest.raises(ValidationError):
        Question(**invalid_question_data)

def test_question_name_length():
    valid_question_data_with_invalid_name = valid_question_data.copy()
    valid_question_data_with_invalid_name["question_name"] = "Q"  
    with pytest.raises(ValidationError):
        Question(**valid_question_data_with_invalid_name)

def test_question_type_pattern():
    valid_question_data_with_invalid_type = valid_question_data.copy()
    valid_question_data_with_invalid_type["question_type"] = "invalidtype"  
    with pytest.raises(ValidationError):
        Question(**valid_question_data_with_invalid_type)

def test_question_options_types():
    invalid_question_options_data = valid_question_data.copy()
    invalid_question_options_data["question_options"] = ["Option A", 123, True]
    with pytest.raises(ValidationError):
        Question(**invalid_question_options_data)