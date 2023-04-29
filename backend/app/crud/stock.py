from fastapi import Depends, HTTPException
from beanie import PydanticObjectId
from app.models.stock import Stock
from app.models.user import User
from app.models.like import StockLike, LikeType
from app.util.current_user import current_user
from datetime import datetime


async def get_all_stocks():
    """Retrieve all stocks from the database."""
    stocks = []
    async for stock in Stock.find():
        stocks.append(stock)
    return stocks


async def get_stock(stock_id: PydanticObjectId):
    stock = await Stock.find_one({"_id": stock_id})
    if not stock:
        raise HTTPException(404, "Stock not found")
    return stock


# Like or dislike a stock
async def like_stock(stock_id: PydanticObjectId, action: LikeType, user: User):
    # Check if the user has already liked or disliked the stock
    existing_like = await StockLike.find_one(
        {"user_id": str(user.id), "stock_id": stock_id}
    )

    if existing_like:
        if existing_like.like_type == action:
            raise HTTPException(400, f"User has already {action}d this stock")
        else:
            # Update the like_type if the user is changing their action
            existing_like.like_type = action
            await existing_like.save()
            return {"message": f"Stock {action}d"}

    # Create a new like document
    like = StockLike(
        user_id=str(user.id),
        stock_id=stock_id,
        like_type=action,
        created_at=datetime.utcnow(),
    )
    await like.insert()

    return {
        "message": f"Stock {action}d",
        "stock_id": stock_id,
        "user_id": user.id,
        "action": action,
    }


# Remove like or dislike for a stock
async def remove_like(stock_id: PydanticObjectId, user: User = Depends(current_user)):
    # Check if the user has liked or disliked the stock
    existing_like = await StockLike.find_one({"user_id": user.id, "stock_id": stock_id})
    if not existing_like:
        raise HTTPException(400, "User has not liked or disliked this stock")

    # Delete the like document
    await existing_like.delete()

    return {"message": "Stock like or dislike removed"}
