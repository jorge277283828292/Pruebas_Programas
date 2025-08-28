from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
modelo = pipeline("text-generation", model="gpt2")

class Prompt(BaseModel):
    texto: str

@app.post("/generar")
def generar_respuesta(prompt: Prompt):
    resultado = modelo(prompt.texto, max_length=50, do_sample=True)[0]['generated_text']
    return {"respuesta": resultado}