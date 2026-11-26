from fastapi import APIRouter, status

from app.dependencies import ProyectoDep, RepositorioDep
from app.schemas import Evaluacion, EvaluacionIn

router = APIRouter(prefix="/proyectos/{proyecto_id}/evaluaciones", tags=["Evaluaciones"])

@router.post("", response_model=Evaluacion, status_code=status.HTTP_201_CREATED)
def crear_evaluacion(proyecto: ProyectoDep, datos: EvaluacionIn, repositorio: RepositorioDep):
    return repositorio.crear_evaluacion(proyecto.id, datos)

@router.get("", response_model=list[Evaluacion])
def listar_evaluaciones(proyecto: ProyectoDep, repositorio: RepositorioDep):
    return repositorio.listar_evaluaciones(proyecto.id)
