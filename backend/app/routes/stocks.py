from fastapi import APIRouter, Depends
from pymongo.database import Database
from app import database, helpers

router = APIRouter()


@router.get("/stocks")
async def get_stocks(db: Database = Depends(database.get_db)):
    stocks_collection = db["stock"]
    stocks = stocks_collection.find()
    data = [stock for stock in stocks]
    stock_data = helpers.convert_objectids_to_strings(data)
    return {"data": data[:10]}
