from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_celsius_para_fahrenheit():
    resposta = client.post("/conversor/temperatura", json={"valor": 0, "de": "celsius"})
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 32, "unidade": "fahrenheit"}

def test_fahrenheit_para_celsius():
    resposta = client.post("/conversor/temperatura", json={"valor": 32, "de": "fahrenheit"})
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 0, "unidade": "celsius"}

def test_km_para_milhas():
    resposta = client.post("/conversor/distancia", json={"valor": 10, "de": "km"})
    assert resposta.status_code == 200
    # round() evita erro de arredondamento de ponto flutuante na comparação
    assert round(resposta.json()["resultado"], 2) == 6.21

def test_unidade_invalida():
    resposta = client.post("/conversor/temperatura", json={"valor": 10, "de": "kelvin"})
    assert resposta.status_code == 200
    assert "erro" in resposta.json()