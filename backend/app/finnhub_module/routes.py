from app import finnhub_module
from fastapi import APIRouter

router = APIRouter()


@router.get("/profile")
async def get_stock_profile(ticker):
    """Get the profile of a stock by its ticker."""
    profile = finnhub_module.services.get_company_profile(ticker)
    return {"data": profile}


@router.get("/sp500")
async def get_sp500_list():
    """Get the list of stock tickers in the S&P 500."""
    sp500_list = finnhub_module.services.get_sp500_list()
    return {"data": sp500_list}
