from sqlalchemy.exc import IntegrityError
from conexao import session
from models_db import Movie, Series

def add_movie(title, year, rating):
    movie = Movie(title=title, year=year, rating=rating)
    try:
        session.add(movie)
        session.commit()
        print(f"Filme '{title}' inserido com sucesso.")
    except IntegrityError:
        session.rollback()
        print(f"Filme '{title}' já existe no banco.")

def add_series(title, year, seasons, episodes):
    series = Series(title=title, year=year, seasons=seasons, episodes=episodes)
    try:
        session.add(series)
        session.commit()
        print(f"Série '{title}' inserida com sucesso.")
    except IntegrityError:
        session.rollback()
        print(f"Série '{title}' já existe no banco.")

def get_movies():
    return session.query(Movie).all()

def get_series():
    return session.query(Series).all()
