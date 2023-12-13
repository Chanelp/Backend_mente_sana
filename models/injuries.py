from config.database import Base, Session

# Orm
from sqlalchemy import Column, Integer, String

class InjuriesModel (Base):

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']

    __tablename__ = 'injuries'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False, unique=True)


    @classmethod
    def create_default_records(self):
        from utils.injuries import PROBLEMAS_PSICOLOGICOS


        try:    
            db = Session()
            if db.query(self).count() != len(PROBLEMAS_PSICOLOGICOS):

                from sqlalchemy.sql import text as sa_text
                db.execute(sa_text(f'DELETE FROM {self.__tablename__}'))
            
                for injurie in PROBLEMAS_PSICOLOGICOS:
                    db.add(InjuriesModel(id=injurie[1], name=injurie[0]))
                
                db.commit()
        except Exception as e:
            print('=== ERROR AL CREAR LAS ENFERMEDADES COMUNES ===')
            print(str(e))