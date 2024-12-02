from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Persona(BaseModel):
    nombre: str
    apellido: str
    edad: int
    dni: int

# http://127.0.0.1:8000/get
@app.get("/personas")
def get_users():
    return [{"id": 1, "name": "John Doe"}]

# Endpoint para obtener un usuario por ID
@app.get("/personas/{id}")
def get_user(id: int):
    return {"id": id, "name": "John Doe"}

# Endpoint para crear un nuevo usuario
@app.post("/personas/crear")
def crear(persona: Persona):
    return {"message": "Usuario {persona.nombre} creado"}

@app.put("/personas/update")
async def modificar(persona_id: int, persona: Persona):
    if persona_id not in get_users[id]:
        raise HTTPException(status_code=404, detail="User no existe")
    return{"message": "Persona {persona_id} modificado"}

@app.delete("/personas/borrar")
def borrar(persona_id: int):
    if persona_id not in get_users[id]:
        raise HTTPException(status_code=404, detail="User no existe")
    usuarioeliminado = get_user.pop(persona_id)
    return{"message": "Persona {usuarioeliminado.get_user} eliminado"}

@app.get("/")
def index ():
    return {"message":"EEEAEEAAE"}