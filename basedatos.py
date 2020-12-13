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

def ingresar_cliente(cliente:Cliente):
    if cliente.cedula in clientes:
        return False
    else:
        clientes[cliente.cedula]= cliente
        return True
        
class Rol(BaseModel):
    id: int
    tipo: str

Roles={
    1: Rol(id=1, tipo="administrador"),
    2: Rol(id=2, tipo="supervisor"),
    3: Rol(id=3, tipo="vendedor")
}
class Usuario(BaseModel):
    cedula:int
    nombre: str
    apellido: str
    alias: str
    password: str
    celular: int
    rol: int

usuarios={
    1: Usuario(cedula=54526581, nombre="sandra", apellido="rey", alias="sandrey", password="54ndr3y", celular=38187417555, rol=1),
    2: Usuario(cedula=54526582, nombre="carlos", apellido="lópez", alias="carlitos1", password="c4rl05", celular=3215467895, rol=3),
}
