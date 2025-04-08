import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def buscar_filme_id(nome):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={nome}"
    response = requests.get(url)
    dados = response.json()
    if dados["results"]:
        filme = dados["results"][0]
        return filme["id"], filme["title"]
    else:
        raise Exception("Filme não encontrado.")

def recomendar_similares(filme_id):
    url = f"https://api.themoviedb.org/3/movie/{filme_id}/recommendations?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    dados = response.json()
    recomendacoes = []
    for item in dados["results"]:
        recomendacoes.append({
            "titulo": item["title"],
            "descricao": item.get("overview", "Sem descrição."),
            "poster_url": f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get("poster_path") else None
        })
    return recomendacoes
