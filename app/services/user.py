"""User create, update, delete services."""

from app import models
from app.schemas.user import UserCreateRequest
from sqlalchemy.orm import Session


def create_user(user_req: UserCreateRequest, db: Session):
    """Create a user."""
    user = models.User(**user_req.dict())
    db.add(user)
    db.commit()
    return user
