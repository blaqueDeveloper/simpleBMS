from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

DB_URI = 'sqlite:///books.db'

engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)  
