from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock, AsyncMock
from main import app

client = TestClient(app)

def test_buscar_filme_padrao():
    """
    Testa a rota /filme sem parâmetros (deve usar o padrão 'Men of Honor').
    Simula a resposta da OMDb API para não fazer requisição real.
    """
    mock_data = {
        "Title": "Men of Honor",
        "Year": "2000",
        "Plot": "The story of Carl Brashear...",
        "Response": "True"
    }

    # Mockamos o httpx.AsyncClient usado dentro da rota
    with patch("httpx.AsyncClient") as mock_client_cls:
        mock_instance = mock_client_cls.return_value
        
        # Configura o context manager (async with httpx.AsyncClient() as client)
        mock_instance.__aenter__.return_value = mock_instance
        mock_instance.__aexit__.return_value = None
        
        # Configura o retorno do método .get()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        
        # Como o .get é awaitable, usamos AsyncMock
        mock_instance.get = AsyncMock(return_value=mock_response)

        # Faz a requisição para a nossa API
        response = client.get("/filme")

    # Verificações (Asserts)
    assert response.status_code == 200
    assert response.json() == mock_data

def test_buscar_filme_nao_encontrado():
    """Testa como a API reage se o serviço externo retornar erro ou filme não encontrado"""
    # Aqui você pode implementar testes para cenários de erro, 
    # por exemplo, se a OMDb retornar {"Response": "False", "Error": "Movie not found!"}
    pass