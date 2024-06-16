import os
import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))


def mock_mongo_client(*args, **kwargs):
    mock_client = MagicMock()
    mock_db = MagicMock()
    mock_db.name = os.getenv("DATABASE_NAME")
    mock_client.__getitem__.return_value = mock_db
    return mock_client


@patch('pymongo.MongoClient', new=mock_mongo_client)
def test_db_connection():
    from config.db import get_db

    db, MONGO_DB_URI, DATABASE_NAME = get_db()

    assert MONGO_DB_URI is not None, "MONGO_DB_URI should not be None"
    assert DATABASE_NAME is not None, "DATABASE_NAME should not be None"

    assert db.name == DATABASE_NAME, "Database name should match the environment variable"
    assert db is not None, "Database instance should not be None"


@patch.dict(os.environ, {"DATABASE_NAME": ""})
def test_missing_database_name():
    from config.db import get_db
    with pytest.raises(ValueError, match="No DATABASE_NAME found in environment variables"):
        get_db()


@patch.dict(os.environ, {"MONGO_DB_URI": ""})
def test_missing_mongo_uri():
    from config.db import get_db
    with pytest.raises(ValueError, match="No MONGO_DB_URI found in environment variables"):
        get_db()
