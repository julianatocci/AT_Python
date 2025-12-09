# AT_Python
# IMDb Top 250 - Scraping e Análise de Filmes e Séries

Este projeto realiza o scraping da página IMDb Top 250, armazena os filmes em um banco de dados SQLite e permite análises simples dos dados. Além disso, exporta os dados para arquivos CSV e JSON.

# Funcionalidades

1. Realiza scraping da página [IMDb Top 250](https://www.imdb.com/chart/top/).
2. Extrai título, ano e nota de cada filme.
3. Cria objetos Python para filmes e séries usando classes (`Movie`, `Series`).
4. Armazena os dados em `imdb.db` usando SQLAlchemy.
5. Consulta os dados.
6. Classifica filmes por categoria de nota.
7. Exibe resumos de filmes por categoria e ano.
8. Exporta os dados para CSV e JSON.


## Pré-requisitos

- Python 3.11+
- Bibliotecas:
  - requests
  - beautifulsoup4
  - pandas
  - sqlalchemy
  - tabulate

Instale todas as dependências usando:
  pip install -r requirements.txt


# Execução

No terminal, entre na pasta src/ e em seguida rode o main.py:
  - cd src
  - python main.py


# Fluxo completo:

- Scraping dos filmes.
- Inserção no banco de dados.
- Criação do catálogo de filmes e séries.
- Análise dos dados e exibição de resumos.
- Exportação para CSV e JSON. 