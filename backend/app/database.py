# Database connection

from pymongo import MongoClient
from pymongo.database import Database
from app import config

mongo_client = MongoClient(config.MONGODB_URI)


def get_db() -> Database:
    db_name = config.MONGODB_DB
    return mongo_client[db_name]
