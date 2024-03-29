"""
User router
"""

from fastapi import APIRouter, Depends, Response
from fastapi_jwt_auth import AuthJWT

from app.models.user import User, UserOut, UserUpdate
from app.util.current_user import current_user

router = APIRouter(tags=["User"])


@router.get("/user", response_model=UserOut)
async def get_user(user: User = Depends(current_user)):
    """Returns the current user"""
    return user


@router.patch("/user", response_model=UserOut)
async def update_user(update: UserUpdate, user: User = Depends(current_user)):
    """Update allowed user fields"""
    user = user.copy(update=update.dict(exclude_unset=True))
    await user.save()
    return user


@router.delete("/user")
async def delete_user(auth: AuthJWT = Depends()):
    """Delete current user"""
    auth.jwt_required()
    await User.find_one(User.email == auth.get_jwt_subject()).delete()
    return Response(status_code=204)
