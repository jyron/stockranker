"""Vote Schemas."""

from pydantic import BaseModel


class VoteCreateRequest(BaseModel):
    user_id: int
    stock_id: int
    type: bool
