from config.database import Base, createAt, Session
from sqlalchemy import Column, String, Integer


class StatusesModel(Base):
    __tablename__ = "statuses"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    status = Column(String, nullable=False)

    createAt = createAt.copy()

    def __init__(self, status, **kwargs):
        self.status = status
        if (kwargs["id"] != None): self.id = kwargs['id']



    @classmethod
    def create_default_records(self):
        try:
            db = Session()
            DEFAULT_STATUSES = [
                ("Disponible"), # ID= 1
                ("En espera",), # ID= 2
                ("No disponible"), # ID = 3
                ("Eliminado"), # ID = 4
                ("En proceso"), # ID = 5
            ]
            statuses_count = db.query(self).count()
            if statuses_count < len(DEFAULT_STATUSES):
                for index in range(statuses_count, len(DEFAULT_STATUSES)):
                    db.add(StatusesModel(DEFAULT_STATUSES[index], id = index + 1)) 
                db.commit()
        except:
            print('=== ERROR AL CREAR ESTADOS ===')
