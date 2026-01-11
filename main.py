from fastapi import FastAPI
import httpx
import os
from dotenv import load_dotenv
from mangum import Mangum

load_dotenv()

app = FastAPI()
handler = Mangum(app)

# Rota para a OMDb API (conforme o link fornecido)
@app.get("/filme")
async def buscar_filme(titulo: str = "Men of Honor"):
    """
    Busca dados de um filme na OMDb API.
    Exemplo: /filme?titulo=Matrix
    """
    # Parâmetros extraídos do link que você enviou
    api_key = os.getenv("OMDB_API_KEY")
    params = {"t": titulo, "plot": "full", "apikey": api_key}
    
    async with httpx.AsyncClient() as client:
        response = await client.get("http://www.omdbapi.com/", params=params)
    
    return response.json()
