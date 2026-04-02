from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"respuesta": "servidor eclipse en linea"}

accion_actual = "encender_led"

@app.get("/comando")
def comando():
    return {"accion": accion_actual}

@app.get("/encender")
def encender():
    global accion_actual
    accion_actual = "encender_led"
    return {"status": "LED encendido"}

@app.get("/apagar")
def apagar():
    global accion_actual
    accion_actual = "apagar_led"
    return {"status": "LED apagado"}
