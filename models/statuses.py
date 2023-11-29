from config.database import Base, createAt
from sqlalchemy import Column, String, Integer


class statuses(Base):
    __tablename__ = "statuses"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    status = Column(String, nullable=False)

    createAt = createAt.copy()