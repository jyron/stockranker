"""
Server app config
"""

# pylint: disable=import-error

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import CONFIG
from app.models.user import User
from app.models.stock import Stock

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins, you can use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # List of allowed methods, you can use ["*"] to allow all
    allow_headers=["*"],  # List of allowed headers, you can use ["*"] to allow all
)


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:4200",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def app_init():
    """Initialize application services"""
    app.db = AsyncIOMotorClient(CONFIG.mongo_uri).stockranker
    await init_beanie(app.db, document_models=[User, Stock])
