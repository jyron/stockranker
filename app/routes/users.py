"""User endpoints."""

from fastapi import APIRouter, Depends
from app import models
from app import services
from app.schemas.user import UserCreateRequest
from app.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    """Return all users."""
    return db.query(models.User).all()


@router.post("/users")
def create_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    """Create a user."""
    return services.user.create_user(user_req=user, db=db)
