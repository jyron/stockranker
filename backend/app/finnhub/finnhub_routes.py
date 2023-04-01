from app.finnhub import finnhub_services
from fastapi import APIRouter

router = APIRouter()


@router.get("/profile")
async def get_stock_profile(ticker):
    profile = finnhub_services.get_company_profile(ticker)
    return {"data": profile}
