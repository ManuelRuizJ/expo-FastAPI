from typing import Annotated

from fastapi import APIRouter, Query, status

from app.dependencies import buscar_proyecto
from app.repository import repositorio
from app.schemas import Evaluacion, EvaluacionIn

router = APIRouter(prefix="/proyectos/{proyecto_id}/evaluaciones", tags=["Evaluaciones"])

@router.post("", response_model=Evaluacion, status_code=201)
def crear_evaluacion(proyecto_id: int, datos: EvaluacionIn):
    buscar_proyecto(proyecto_id)
    return repositorio.crear_evaluacion(proyecto_id, datos)

@router.get("", response_model=list[Evaluacion])
def listar_evaluaciones(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repositorio.listar_evaluaciones(proyecto_id)


