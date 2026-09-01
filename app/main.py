from fastapi import FastAPI
from app.calculadora import router as calculadora_router
from app.conversor import router as conversor_router

# Cria a aplicação FastAPI
app = FastAPI(title="Calculadora e Conversor de Unidades")

# Adiciona as rotas da calculadora e do conversor
app.include_router(calculadora_router)
app.include_router(conversor_router)


# Rota principal da API
@app.get("/")
def raiz():
    return {"mensagem": "API de Calculadora e Conversor de Unidades no ar!"}