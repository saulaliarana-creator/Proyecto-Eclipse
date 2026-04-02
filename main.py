from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

accion_actual = "apagar_led"

@app.get("/")
def home():
    return {"respuesta": "servidor eclipse en linea"}

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

@app.get("/control", response_class=HTMLResponse)
def control():
    return """
    <html>
    <head>
        <title>Proyecto Eclipse</title>
    </head>
    <body style="text-align:center; font-family:Arial;">
        <h1>🌑 Proyecto Eclipse</h1>
        <h2>Control de LED</h2>

        <button onclick="fetch('/encender')" style="padding:20px; font-size:20px;">
            ENCENDER
        </button>

        <br><br>

        <button onclick="fetch('/apagar')" style="padding:20px; font-size:20px;">
            APAGAR
        </button>
    </body>
    </html>
    """
