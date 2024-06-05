from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.sql import func
from datetime import datetime

class Compute(Base):
    __tablename__ = "transactions"
    batch_id: str = Column(String(100), primary_key=True, index=True)
    input: str = Column(String(5000))
    output: str = Column(String(5000))
    created_at: datetime = Column(
        TIMESTAMP(timezone=True),
        nullable=False, server_default=func.now()
    )
