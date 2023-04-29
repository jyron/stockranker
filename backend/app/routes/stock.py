from app.crud.stock import get_all_stocks, get_stock, like_stock
from app.models.user import User
from app.util.current_user import current_user
from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

router = APIRouter(tags=["Stock"])


@router.get("/stocks", response_description="Stocks retrieved")
async def get_stocks_route():
    """Retrieve all stocks from the database."""
    try:
        stocks = await get_all_stocks()
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Stocks data retrieved successfully",
            "data": stocks,
        }
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@router.get("/stocks/{stock_id}", response_description="Stock retrieved")
async def get_stock_route(stock_id: str):
    """Retrieve a stock from the database."""
    try:
        stock = await get_stock(stock_id)
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Stock data retrieved successfully",
            "data": stock,
        }
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@router.post("/stocks/{stock_id}/like/{action}")
async def like_stock_route(
    stock_id: str, action: str, user: User = Depends(current_user)
):
    try:
        like = await like_stock(stock_id, action, user)
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Stock liked successfully",
            "data": like,
        }
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
