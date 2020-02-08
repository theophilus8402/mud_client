
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base_path = os.path.dirname(__file__)
engine = create_engine(f"sqlite:///{base_path}/rooms.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

