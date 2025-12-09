from models import Movie, Series
from crud import add_movie, add_series
from conexao import engine
from models_db import Base
from consultas import get_movies_df, get_series_df, classificar_nota
from tabulate import tabulate
from scraping import obter_filmes
from exportacao import *
from caminhos_constantes import CONFIG_JSON
import json 

Base.metadata.create_all(engine)

with open(CONFIG_JSON, "r", encoding="utf-8") as json_file:
    config = json.load(json_file)

url = config.get("url_imdb_top")
n_filmes = config.get("n_filmes")
filmes_scraped = obter_filmes(url, n_filmes)

catalogo = []

for filme in filmes_scraped:
    nota = float(filme["nota"].replace(",", ".")) if filme["nota"] != "N/A" else 0.0
    catalogo.append(Movie(filme["titulo"], filme["ano"], nota))
    add_movie(filme["titulo"], filme["ano"], nota)
  
series_ficticias = [
  Series("Breaking Bad", 2008, 5, 62),
  Series("Stranger Things", 2016, 5, 45)
]

for serie in series_ficticias:
    catalogo.append(serie)
    add_series(serie.title, serie.year, serie.seasons, serie.episodes)

print("\nSéries e Filmes: ")
for item in catalogo:
    print(item)

df_movies = get_movies_df()
df_movies["categoria"] = df_movies["rating"].apply(classificar_nota)

df_to_show = df_movies[["title", "rating", "categoria"]].head(10)
print(f"\n{df_to_show}")

resumo = df_movies.groupby(["categoria", "year"]).size().reset_index(name="quantidade")
print(tabulate(resumo, headers="keys", showindex=False))

export_csv(df_movies, "data/movies.csv")
export_csv(get_series_df(), "data/series.csv")
export_json(df_movies, "data/movies.json")
export_json(get_series_df(), "data/series.json")
