"""Stock create, update, delete services."""
from sqlalchemy.orm import Session

from app.models import Stock
from app.schemas.stock import StockCreateRequest


def create_stock(stock_req: StockCreateRequest, db: Session):
    """Create a stock."""
    stock = Stock(**stock_req.dict())
    db.add(stock)
    db.commit()
    return stock
