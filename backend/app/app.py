"""
Server app config
"""

# pylint: disable=import-error

from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import CONFIG
from app.models.user import User

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins, you can use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # List of allowed methods, you can use ["*"] to allow all
    allow_headers=["*"],  # List of allowed headers, you can use ["*"] to allow all
)


@app.on_event("startup")
async def app_init():
    """Initialize application services"""
    app.db = AsyncIOMotorClient(CONFIG.mongo_uri).stockranker
    await init_beanie(app.db, document_models=[User])
