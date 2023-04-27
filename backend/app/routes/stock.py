from fastapi import APIRouter, Response
from app.crud.stock import retrieve_stocks

router = APIRouter(tags=["Stock"])


@router.get("/stocks", response_description="Stocks retrieved")
async def get_stocks():
    """Retrieve all stocks from the database."""
    stocks = await retrieve_stocks()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Stocks data retrieved successfully",
        "data": stocks,
    }
