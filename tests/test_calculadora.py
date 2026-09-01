from fastapi.testclient import TestClient
from app.main import app
# Cliente de teste simula requisições HTTP sem precisar rodar o servidor
client = TestClient(app)

def test_somar():
    resposta = client.post("/calculadora/somar", json={"a": 2, "b": 3})
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 5}

def test_subtrair():
    resposta = client.post("/calculadora/subtrair", json={"a": 5, "b": 3})
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 2}

def test_multiplicar():
    resposta = client.post("/calculadora/multiplicar", json={"a": 4, "b": 3})
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 12}

def test_dividir():
    resposta = client.post("/calculadora/dividir", json={"a": 10, "b": 2})
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 5}

def test_dividir_por_zero():
    resposta = client.post("/calculadora/dividir", json={"a": 10, "b": 0})
    assert resposta.status_code == 200
    assert resposta.json() == {"erro": "Divisão por zero não é permitida"}