from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
class Compute(Base):
    __tablename__ = "transactions"
    id: int = Column(String(100), primary_key=True, index=True)
    input: str = Column(String(5000))
    output: str = Column(String(5000))
    created_at: str = Column(DateTime(timezone=True), default=datetime.datetime.now(datetime.UTC))