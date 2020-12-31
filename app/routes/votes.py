"""Vote endpoints."""

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app import models

from app import services
from app.schemas.vote import VoteCreateRequest

router = APIRouter()


@router.get("/votes")
def get_votes(db: Session = Depends(get_db)):
    """Return all votes."""
    return db.query(models.Vote).all()


@router.post("/votes")
def create_vote(vote: VoteCreateRequest, db: Session = Depends(get_db)):
    """Create a vote."""
    return services.vote.create_vote(vote_req=vote, db=db)
