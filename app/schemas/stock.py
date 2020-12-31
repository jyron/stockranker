"""Stock Pydantic schemas."""

from pydantic import BaseModel


class StockCreateRequest(BaseModel):
    name: str
    price: float
    sector: str
    symbol: str
