import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de la calculadora básica"}

@app.get("/sumar/")
def sumar(a: float, b: float):
    return {"resultado": a + b}

@app.get("/restar/")
def restar(a: float, b: float):
    return {"resultado": a - b}

@app.get("/multiplicar/")
def multiplicar(a: float, b: float):
    return {"resultado": a * b}

@app.get("/dividir/")
def dividir(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir por cero")
    return {"resultado": a / b}

if __name__ == "__main__":
    print("Iniciando servidor...")   
    uvicorn.run("calculator.main:app", host="127.0.0.1", port=8000, reload=True)