from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import clientes_db
from db import usuarios_db
from models.clientes_modelo import *
from models.usuario_modelo import UserIn, UserStatus


app= FastAPI()
userstatus = UserStatus()

@app.post("/usuario/login/")
async def auth_user(user_in: UserIn):
    user_in_db = usuarios_db.obtener_usuario(user_in.cedula)
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        userstatus.autenticado = False
        return {"mensaje": "El password no corresponde"}
    userstatus.autenticado = True
    return {"mensaje": "Bienvenid@ "+user_in_db.nombre}

#Petición a una ruta
@app.get("/clientes/lista/")
#Asincrona, la función no se ejecuta constantemente con las demas funciones 
async def enlistar_clientes():
    #Devuelve el codigo http 200
    return  clientes_db.lista_clientes()

@app.post("/clientes/agregar/")
async def agregar_cliente(cliente: clientes_db.ClienteDb):
    if userstatus.autenticado:
        operacion_exitosa = clientes_db.ingresar_cliente(cliente)
        if operacion_exitosa:
            return {"mensaje":"Cliente creado"}
        else:
            raise HTTPException(status_code=400, detail="Cliente existente")
    return {"mensaje":"Debe autenticarse"} 

@app.get("/usuarios/listado/")
async def enlistar_usuarios():
    #Devuelve el codigo http 200
    return  usuarios_db.lista_usuarios()

@app.post("/clientes/buscar/")
async def buscar_clientes(cliente: BuscarClienteCedula):
    if userstatus.autenticado:
        operacion_exitosa = clientes_db.buscar_cliente(cliente.cedula)
        if operacion_exitosa:
            return operacion_exitosa
        else:
            raise HTTPException(status_code=400, detail="Cliente no existe")
    return {"mensaje":"Debe autenticarse"}


