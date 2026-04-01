from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"respuesta": "servidor eclipse en linea"}

@app.get("/comando")
def comando():
    return {"accion": "encender_led"}