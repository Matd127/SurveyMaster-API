from models.tag import Tag  # Upewnij się, że ścieżka do modułu Tag jest poprawna
import pytest
from pydantic import ValidationError
from bson import ObjectId
import json


def test_valid_tag():
    tag = Tag(name="valid_tag")
    assert isinstance(tag, Tag)
    assert tag.name == "valid_tag"
    assert isinstance(tag.id, ObjectId)

def test_name_too_short():
    with pytest.raises(ValidationError) as exc_info:
        Tag(name="ab")
    assert 'String should have at least 3 characters' in str(exc_info.value)

def test_name_too_long():
    with pytest.raises(ValidationError) as exc_info:
        Tag(name="a" * 51)
    assert 'String should have at most 50 characters' in str(exc_info.value)

def test_name_not_alphanumeric():
    with pytest.raises(ValidationError) as exc_info:
        Tag(name="invalid tag!")
    assert 'must contain only letters, numbers, and underscores' in str(exc_info.value)

def test_default_id_generation():
    tag = Tag(name="valid_tag")
    assert isinstance(tag.id, ObjectId)

def test_custom_id():
    custom_id = ObjectId()
    tag = Tag(id=custom_id, name="valid_tag")
    assert tag.id == custom_id

def test_json_encoding():
    tag = Tag(name="valid_tag")
    tag_json = tag.model_dump_json()
    tag_dict = json.loads(tag_json)
    
    assert str(tag.id) == tag_dict['id']
    assert tag_dict['name'] == "valid_tag"