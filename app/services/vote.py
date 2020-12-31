"""Vote create, update, delete services."""

from app.schemas.vote import VoteCreateRequest
from app import models
from sqlalchemy.orm import Session


def create_vote(vote_req: VoteCreateRequest, db: Session):
    """Create a vote."""
    vote = models.Vote(**vote_req.dict())
    db.add(vote)
    db.commit()
    return vote
