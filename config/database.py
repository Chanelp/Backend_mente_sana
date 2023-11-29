import os
from sqlalchemy import create_engine, event, Table, Column, DateTime
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo = True)

Session = sessionmaker(bind = engine)

Base = declarative_base()


# Default column to all tables
createAt = Column(DateTime, nullable=False, default=datetime.now)
createdDate = Column(DateTime, nullable=False, default=datetime.now)


def addCreationDate(mapper, connect, target):
    # add new date
    target.createAt = DateTime()

# Hook that create a default value to new data
event.listen(Base, 'before_insert', addCreationDate)

