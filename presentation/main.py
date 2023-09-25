# presentation/api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from application.use_case import CalcularCompraMilhasUseCase
from persistence.models import CompraMilhas

app = FastAPI()

class DadosCompraMilhas(BaseModel):
    milhas_comprar: int
    desconto: int
    bonus: int

@app.post("/calcular_compra_milhas")
async def calcular_compra_milhas(dados: DadosCompraMilhas):
    compra_milhas = CompraMilhas(
        milhas_comprar=dados.milhas_comprar,
        desconto=dados.desconto,
        bonus=dados.bonus,
    )
    resultado = CalcularCompraMilhasUseCase.calcular_compra(compra_milhas)
    return resultado

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
