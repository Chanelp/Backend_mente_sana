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
                ("Disponible", 1), # ID= 1
                ("En espera", 2), # ID= 2
                ("No disponible", 3), # ID= 3
            ]
            if db.query(self).count() != len(DEFAULT_STATUSES):
                from sqlalchemy.sql import text as sa_text
                db.execute(sa_text('''DELETE FROM statuses'''))
                for defaulValue in DEFAULT_STATUSES:
                    db.add(StatusesModel(defaulValue[0], id = defaulValue[1])) 
                db.commit()
        except:
            print('=== ERROR AL CREAR ESTADOS ===')
