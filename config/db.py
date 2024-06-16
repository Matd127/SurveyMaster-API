import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_db():
    MONGO_DB_URI = os.getenv('MONGO_DB_URI')
    DATABASE_NAME = os.getenv("DATABASE_NAME")

    if not DATABASE_NAME:
        raise ValueError("No DATABASE_NAME found in environment variables")

    if not MONGO_DB_URI:
        raise ValueError("No MONGO_DB_URI found in environment variables")

    client = MongoClient(MONGO_DB_URI)
    db = client[DATABASE_NAME]
    return db, MONGO_DB_URI, DATABASE_NAME


db, MONGO_DB_URI, DATABASE_NAME = get_db()
