from app import helpers
from pymongo.database import Database


def get_all_stocks(db: Database):
    """Get all stocks from the database."""
    stocks_collection = db["stock"]
    stocks = stocks_collection.find()
    data = [stock for stock in stocks]
    stock_data = helpers.convert_objectids_to_strings(data)
    return stock_data

# get stockby ticker


def get_stock_by_ticker(db: Database, ticker: str):
    """Get a stock by its ticker."""
    stocks_collection = db["stock"]
    stock = stocks_collection.find_one({"ticker": ticker})
    stock_data = helpers.convert_objectids_to_strings([stock])
    return stock_data
