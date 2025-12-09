from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    year = Column(String)
    rating = Column(Float)

class Series(Base):
    __tablename__ = "series"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    year = Column(String)
    seasons = Column(Integer)
    episodes = Column(Integer)
