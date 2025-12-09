import requests
from bs4 import BeautifulSoup

def obter_filmes(url, n_filmes=25):
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/142.0.0.0 Safari/537.36"
  }

  response = requests.get(url, headers=headers)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")

  filmes = []

  filmes_divs = soup.select("div.ipc-metadata-list-summary-item__c")

  for filme_div in filmes_divs:
      titulo_tag = filme_div.select_one("h3.ipc-title__text")
      titulo = titulo_tag.get_text(strip=True) if titulo_tag else "N/A"

      ano_tag = filme_div.select_one("span.cli-title-metadata-item")
      ano = ano_tag.get_text(strip=True) if ano_tag else "N/A"

      nota_tag = filme_div.select_one("span.ipc-rating-star--rating")
      nota = nota_tag.get_text(strip=True) if nota_tag else "N/A"

      filmes.append({
          "titulo": titulo,
          "ano": ano,
          "nota": nota
      })
  
  return filmes

# for f in filmes[:5]:
#     print(f"{f['titulo']} ({f['ano']}) – Nota: {f['nota']}")