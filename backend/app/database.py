# Database connection

from app import config
from fastapi.params import Depends
from pymongo import MongoClient
from pymongo.database import Database

mongo_client = MongoClient(config.MONGODB_URI)


def get_mongo_client() -> MongoClient:
    return mongo_client


def get_db(client: MongoClient = Depends(get_mongo_client)) -> Database:
    return client["stockranker"]
