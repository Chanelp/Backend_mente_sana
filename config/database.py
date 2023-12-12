import os
from sqlalchemy import create_engine, Column, DateTime
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

from utils.env import read_env_key


database_url = read_env_key('DB_URL') or f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo = True)

Session = sessionmaker(bind = engine)

Base = declarative_base()


# Default column to all tables
createAt = Column(DateTime, nullable=False, default=datetime.now)



