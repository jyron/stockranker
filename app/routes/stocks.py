"""Stock endpoints."""

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.dependencies import get_db
from app import models
from app import services
from app.schemas.stock import StockCreateRequest

router = APIRouter()


@router.get("/stocks")
def get_stocks(db: Session = Depends(get_db)):
    """Return all stocks"""
    return db.query(models.Stock).all()


@router.post("/stocks")
def create_stock(stock: StockCreateRequest, db: Session = Depends(get_db)):
    """Create a stock."""
    return services.stock.create_stock(stock_req=stock, db=db)
