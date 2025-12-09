import pandas as pd
from conexao import engine

def get_movies_df():
    try:
        return pd.read_sql("SELECT * FROM movies", con=engine)
    except Exception as e:
        print("Erro ao ler tabela movies:", e)
        return pd.DataFrame()

def get_series_df():
    try:
        return pd.read_sql("SELECT * FROM series", con=engine)
    except Exception as e:
        print("Erro ao ler tabela series:", e)
        return pd.DataFrame()

def get_top_movies(min_rating=9.0, top_n=5):
    df = get_movies_df()
    df_sorted = df.sort_values(by="rating", ascending=False)
    return df_sorted[df_sorted["rating"] > min_rating].head(top_n)

def get_first_lines():
    try:
        df_movies = get_movies_df()
        print(f"Primeiras 5 linhas da tabela movies:\n{df_movies.head()}\n")

        df_series = get_series_df()
        print(f"Primeiras 5 linhas da tabela series:\n{df_series.head()}\n")

    except Exception as e:
        print(f"Ocorreu um erro ao acessar o banco ou ler os dados: {e}")

def classificar_nota(nota):
    if nota >= 9.0:
        return "Obra-prima"
    elif 8.0 <= nota < 9.0:
        return "Excelente"
    elif 7.0 <= nota < 8.0:
        return "Bom"
    else:
        return "Mediano"