from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    cedula:int
    nombre: str
    apellido:str
    telefono: int
    email: Optional[str]=None
    direccion: Optional[str]=None


clientes = {

    1: Cliente(cedula=1, nombre="Laura", apellido="Valencia", telefono=1234, email="por@example.com"),
    2: Cliente(cedula=2, nombre="Ana", apellido="Perez", telefono=7534,email="por456@example.com"),
    3: Cliente(cedula=3, nombre="Marcos", apellido="Avila", telefono=9876, email="por123@example.com")
}

def lista_clientes():
    lista_clientes = []
    for cliente in clientes:
        lista_clientes.append(clientes[cliente])
    return lista_clientes

def buscar_cliente(cedula):
    if cedula in clientes:
        return clientes[id]
    else:
        return None

def ingresar_cliente(clientes:Cliente):
    if cliente.cedula in clientes:
        return False
    else:
        clientes[cliente.cedula]= cliente
        return True

