from fastapi import APIRouter
from pydantic import BaseModel

# Define as rotas de conversão
router = APIRouter(prefix="/conversor", tags=["Conversor"])


# Dados para conversão de temperatura
class TemperaturaRequest(BaseModel):
    valor: float
    de: str


# Dados para conversão de distância
class DistanciaRequest(BaseModel):
    valor: float
    de: str


# Converte entre Celsius e Fahrenheit
@router.post("/temperatura")
def converter_temperatura(dados: TemperaturaRequest):
    if dados.de.lower() == "celsius":
        resultado = (dados.valor * 9 / 5) + 32
        return {"resultado": resultado, "unidade": "fahrenheit"}

    elif dados.de.lower() == "fahrenheit":
        resultado = (dados.valor - 32) * 5 / 9
        return {"resultado": resultado, "unidade": "celsius"}

    # Verifica se a unidade informada é válida
    return {"erro": "Unidade inválida. Use 'celsius' ou 'fahrenheit'"}


# Converte entre quilômetros e milhas
@router.post("/distancia")
def converter_distancia(dados: DistanciaRequest):
    if dados.de.lower() == "km":
        resultado = dados.valor * 0.621371
        return {"resultado": resultado, "unidade": "milhas"}

    elif dados.de.lower() == "milhas":
        resultado = dados.valor / 0.621371
        return {"resultado": resultado, "unidade": "km"}

    # Verifica se a unidade informada é válida
    return {"erro": "Unidade inválida. Use 'km' ou 'milhas'"}