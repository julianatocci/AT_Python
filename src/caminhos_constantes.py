import os

PASTA_DATA = "../data"
if not os.path.exists(PASTA_DATA):
    os.makedirs(PASTA_DATA)

BANCO = os.path.join(PASTA_DATA, "imdb.db")

MOVIES_CSV = os.path.join(PASTA_DATA, "movies.csv")
SERIES_CSV = os.path.join(PASTA_DATA, "series.csv")

MOVIES_JSON = os.path.join(PASTA_DATA, "movies.json")
SERIES_JSON = os.path.join(PASTA_DATA, "series.json")

CONFIG_JSON = os.path.join("..", "config.json")