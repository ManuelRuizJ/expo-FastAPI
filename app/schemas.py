from enum import Enum
from pydantic import BaseModel, Field



class Categoria(str, Enum):
    software = "Software"
    hardware = "Hardware"
    social = "Social"
    ia = "Inteligencia Artificial"

class ProyectoIn(BaseModel):
    nombre: str = Field(min_length=3, max_length=120)
    equipo: list[str] = Field(min_length=1, max_length=5)
    categoria: Categoria

class Proyecto(ProyectoIn):
    id: int