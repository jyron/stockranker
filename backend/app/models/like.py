from datetime import datetime
from enum import Enum

from beanie import Document, Indexed
from pydantic import BaseModel


class LikeType(str, Enum):
    like = "like"
    dislike = "dislike"


class StockLike(Document):
    user_id: str
    stock_id: str
    like_type: LikeType
    created_at: datetime

    class Settings:
        name = "StockLike"
