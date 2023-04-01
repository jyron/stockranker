from app import database, helpers
from app.services import stocks
from fastapi import APIRouter
from fastapi.params import Depends
from pymongo.database import Database

router = APIRouter()


@router.get("/stocks")
async def get_all_stocks(db: Database = Depends(database.get_db)):
    """Get all stocks from the database."""
    stock_data = stocks.get_all_stocks(db)
    return {"data": stock_data}


@router.get("/stocks/{ticker}")
async def get_stock_by_ticker(ticker: str, db: Database = Depends(database.get_db)):
    """Get a stock by its ticker."""
    stock_data = stocks.get_stock_by_ticker(db, ticker)
    return {"data": stock_data}
