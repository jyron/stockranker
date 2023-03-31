# Database connection

from pymongo import MongoClient
from pymongo.database import Database
from fastapi import Depends
from app import config

mongo_client = MongoClient(config.MONGODB_CONNECTION_STRING)


def get_mongo_client() -> MongoClient:
    return mongo_client


def get_db(client: MongoClient = Depends(get_mongo_client)) -> Database:
    return client["stockranker"]
