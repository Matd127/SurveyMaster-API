import pytest
from pydantic import ValidationError
from bson import ObjectId
from models.answer import Answer

valid_answer_data = {
    "question_id": ObjectId(),
    "answer_value": "Sample answer"
}

invalid_answer_data = {
    "question_id": "invalid_object_id",
    "answer_value": ["Option A", "Option B"]
}

def test_create_answer_valid():
    answer = Answer(**valid_answer_data)
    assert answer
    assert isinstance(answer.id, ObjectId)

def test_create_answer_invalid():
    with pytest.raises(ValidationError):
        Answer(**invalid_answer_data)

def test_answer_value_optional():
    answer_data_without_value = {
        "question_id": ObjectId(),
        "answer_value": None  
    }
    answer = Answer(**answer_data_without_value)
    assert answer
    assert answer.answer_value is None

def test_answer_value_union_str():
    answer_data_with_str_value = {
        "question_id": ObjectId(),
        "answer_value": "Single answer"
    }
    answer = Answer(**answer_data_with_str_value)
    assert answer

def test_answer_value_union_list():
    answer_data_with_list_value = {
        "question_id": ObjectId(),
        "answer_value": ["Option A", "Option B"]
    }
    answer = Answer(**answer_data_with_list_value)
    assert answer

def test_answer_id_generation():
    answer = Answer(question_id=ObjectId(), answer_value=None)
    assert answer
    assert isinstance(answer.id, ObjectId)