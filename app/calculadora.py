from fastapi import APIRouter
from pydantic import BaseModel

# Define as rotas da calculadora
router = APIRouter(prefix="/calculadora", tags=["Calculadora"])


# Dados recebidos nas operações
class OperacaoRequest(BaseModel):
    a: float
    b: float


# Soma dois números
@router.post("/somar")
def somar(dados: OperacaoRequest):
    return {"resultado": dados.a + dados.b}


# Subtrai dois números
@router.post("/subtrair")
def subtrair(dados: OperacaoRequest):
    return {"resultado": dados.a - dados.b}


# Multiplica dois números
@router.post("/multiplicar")
def multiplicar(dados: OperacaoRequest):
    return {"resultado": dados.a * dados.b}


# Divide dois números
@router.post("/dividir")
def dividir(dados: OperacaoRequest):
    # Evita divisão por zero
    if dados.b == 0:
        return {"erro": "Divisão por zero não é permitida"}
    return {"resultado": dados.a / dados.b}