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

class EvaluacionIn(BaseModel):
    innovacion: int = Field(ge=1, le=5)
    viabilidad: int = Field(ge=1, le=5)
    presentacion: int = Field(ge=1, le=5)
    general: int = Field(ge=1, le=5)

class Evaluacion(EvaluacionIn):
    id: int
    proyecto_id: int

class Resumen(BaseModel):
    proyecto_id: int
    total_evaluaciones: int
    innovacion: float | None
    vabilidad: float | None
    presentacion: float | None
    general: float | None