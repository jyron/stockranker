from typing import Optional

from pydantic import BaseModel


class StockInfo(BaseModel):
    country: str
    currency: str
    estimateCurrency: str
    exchange: str
    finnhubIndustry: str
    ipo: str
    logo: str
    marketCapitalization: float
    name: str
    phone: Optional[float]
    shareOutstanding: float
    ticker: str
    weburl: str


class FinnhubResponse(BaseModel):
    data: StockInfo
