from fastapi import FastAPI
from pydantic import BaseModel
from automation import google_search
app = FastAPI()

#Crie abaixo as suas classes de modelo
class Termo(BaseModel):
    term: str
    description: str | None = None

#verifica a saude da API
@app.get("/") 
def saude():
    return {"API": "Funcionando Corretamente"}

#informações do projeto - versão e tecnologias usadas
@app.get("/info")
def info():
    return {
        "project": "FastAPI + Selenium Demo",
        "description": "API with Selenium automation",
        "version": "1.0.0"
    }

#post
@app.post("/search")
def procura_termo(term: Termo):
    result = google_search(term.term)
    return {
        "received_term": term.term,
        "result": result
    }
