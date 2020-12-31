from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from datetime import datetime
from app.database import Base


class Vote(Base):
    __tablename__ = "votes"
    stock_id = Column(Integer, ForeignKey("stock.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now())
    type = Column(Boolean)
