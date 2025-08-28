from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Cargar el modelo de lenguaje
modelo = pipeline("text-generation", model="distilgpt2")

# Modelo de entrada
class EntradaTexto(BaseModel):
    texto: str

# Endpoint para generar texto
@app.post("/generar")
def generar_respuesta(entrada: EntradaTexto):
    resultado = modelo(entrada.texto, max_length=50, num_return_sequences=1)
    return {"respuesta": resultado[0]['generated_text']}
