from typing import Annotated

from fastapi import APIRouter, Query, status

from app.dependencies import buscar_proyecto
from app.repository import repositorio
from app.schemas import Categoria, Proyecto, ProyectoIn, Resumen

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])

@router.post("", response_model=Proyecto, status_code=status.HTTP_201_CREATED)
def crear_proyecto(datos: ProyectoIn):
    return repositorio.crear_proyecto(datos)

@router.get("", response_model=list[Proyecto])
def listar_proyectos(
    categoria: Categoria | None,
    limite: Annotated[int, Query(ge=1, le=100)] =10 
):
    return repositorio.listar_proyectos(categoria, limite)


@router.get("/{proyecto_id}", response_model=Proyecto)
def obtener_proyecto(proyecto_id: int):
    return buscar_proyecto(proyecto_id)


@router.get("/{proyecto_id}/resumen", response_model=Resumen)
def resumen_proyecto(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repositorio.resumen(proyecto_id)
