from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from db import clientes_db
from db import usuarios_db
from models.clientes_modelo import *
from models.usuario_modelo import UserIn, UserStatus

from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080",
    "https://factapp412.herokuapp.com/"
]
app.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

userstatus = UserStatus()

def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

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


