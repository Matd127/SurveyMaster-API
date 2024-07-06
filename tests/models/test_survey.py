import pytest
from pydantic import ValidationError
from bson import ObjectId
from datetime import datetime, timedelta
from models.survey import Survey

valid_survey_data = {
    "title": "Sample Survey",
    "description": "This is a sample survey",
    "start_date": datetime(2024, 1, 1),
    "end_date": datetime(2024, 1, 10),
    "is_open": True,
    "owner": ObjectId(),
    "tags": [ObjectId(), ObjectId()]
}

invalid_survey_data = {
    "title": "A",  # Title too short
    "description": "Short description",
    "start_date": datetime.now(),
    "end_date": datetime.now() - timedelta(days=7),
    "is_open": True,
    "owner": ObjectId(),
    "tags": [ObjectId(), "invalid_object_id"]
}


def test_create_survey_valid():
    survey = Survey(**valid_survey_data)
    assert survey


def test_create_survey_invalid():
    with pytest.raises(ValidationError):
        Survey(**invalid_survey_data)


def test_title_alphanumeric():
    valid_survey_data_with_invalid_title = valid_survey_data.copy()
    valid_survey_data_with_invalid_title["title"] = "Invalid!@#$%^&*"
    with pytest.raises(ValidationError):
        Survey(**valid_survey_data_with_invalid_title)
