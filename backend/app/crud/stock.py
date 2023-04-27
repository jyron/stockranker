from app.models.stock import Stock
from app.models.user import User


# function to retrieve all stocks from the database
async def retrieve_stocks():
    """Retrieve all stocks from the database."""
    stocks = []
    async for stock in Stock.find():
        stocks.append(stock)
    return stocks
