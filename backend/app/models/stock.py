from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from beanie import Document


class Price(BaseModel):
    c: float
    d: float
    dp: float
    h: float
    l: float
    o: float
    pc: float
    t: int


class Stock(Document):
    country: str
    currency: str
    exchange: str
    industry: Optional[str]
    ipo: Optional[str]
    logo: str
    market_cap: float
    name: str
    phone: str
    share_outstanding: float
    ticker: str
    weburl: str
    price: Price
    likes: int
    dislikes: int
    comments: list
    likes_count: Optional[int] = None

    class Settings:
        name = "stock"
