from config.database import Base, createAt, Session
from sqlalchemy import Column, String, Integer


class StatusesModel(Base):
    __tablename__ = "statuses"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    status = Column(String, nullable=False)

    createAt = createAt.copy()

    def __init__(self, status):
        self.status = status


    @classmethod
    def create_default_records(self):
        db = Session()
        if not db.query(self).first():
            db.add(StatusesModel("Disponible"))
            db.add(StatusesModel("En espera"))
            db.add(StatusesModel("No disponible"))
            db.commit()