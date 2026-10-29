from enum import Enum
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from app.schemas import Categoria, Proyecto, ProyectoIn, Evaluacion, EvaluacionIn, Resumen
from app.repository import repositorio

app = FastAPI(title="Evaluación Expo Ibero")



def buscar_proyecto(proyecto_id: int) -> Proyecto:
    proyecto = repositorio.obtener_proyecto(proyecto_id)
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo desde FASTAPI :)"}


@app.post("/proyectos", response_model=Proyecto, status_code=201)
def crear_proyecto(datos: ProyectoIn):
    return repositorio.crear_proyecto(datos)


@app.get("/proyectos", response_model=list[Proyecto])
def listar_proyectos(
    categoria: Categoria | None,
    limite: Annotated[int, Query(ge=1, le=100)] =10 
):
    return repositorio.listar_proyectos(categoria, limite)


@app.get("/proyectos/{proyecto_id}", response_model=Proyecto)
def obtener_proyecto(proyecto_id: int):
    return buscar_proyecto(proyecto_id)


@app.post("/proyectos/{proyecto_id}/evaluaciones", response_model=Evaluacion, status_code=201)
def crear_evaluacion(proyecto_id: int, datos: EvaluacionIn):
    buscar_proyecto(proyecto_id)
    return repositorio.crear_evaluacion(proyecto_id, datos)


@app.get("/proyectos/{proyecto_id}/evaluaciones", response_model=list[Evaluacion])
def listar_evaluaciones(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repositorio.listar_evaluaciones(proyecto_id)

@app.get("/proyectos/{proyecto_id}/resumen", response_model=Resumen)
def resumen_proyecto(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repositorio.resumen(proyecto_id)