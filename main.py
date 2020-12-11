from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import basedatos as bd

app= FastAPI()

#Petición a una ruta
@app.get("/clientes/lista")

#Asincrona, la función no se ejecuta constantemente con las demas funciones 
async def enlistar_clientes():
    #Devuelve el codigo http 200
    return  bd.lista_clientes()

#@app.post("/clientes/agregar/")

#async def agregar_cliente(cliente: Cliente):
