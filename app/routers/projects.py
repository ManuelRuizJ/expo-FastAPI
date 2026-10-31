from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import func, select

from app.dependencies import SessionDep, buscar_proyecto
from app.models import EvaluationModel, ProjectModel
from app.schemas import Categoria, Proyecto, ProyectoIn, Resumen

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])


@router.post("", response_model=Proyecto, status_code=status.HTTP_201_CREATED)
async def crear_proyecto(datos: ProyectoIn, session: SessionDep):
    proyecto = ProjectModel(
        nombre=datos.nombre,
        equipo=datos.equipo,
        categoria=datos.categoria.value,
    )
    session.add(proyecto)
    await session.commit()
    await session.refresh(proyecto)
    return proyecto


@router.get("", response_model=list[Proyecto])
async def listar_proyectos(
    session: SessionDep,
    categoria: Categoria | None = None,
    limite: Annotated[int, Query(ge=1, le=100)] = 10,
):
    consulta = select(ProjectModel)
    if categoria is not None:
        consulta = consulta.where(ProjectModel.categoria == categoria.value)
    consulta = consulta.order_by(ProjectModel.id).limit(limite)
    resultado = await session.execute(consulta)
    return resultado.scalars().all()


@router.get("/{proyecto_id}", response_model=Proyecto)
async def obtener_proyecto(
    proyecto: Annotated[ProjectModel, Depends(buscar_proyecto)],
):
    return proyecto


@router.get("/{proyecto_id}/resumen", response_model=Resumen)
async def resumen_proyecto(
    proyecto: Annotated[ProjectModel, Depends(buscar_proyecto)],
    session: SessionDep,
):
    consulta = select(
        func.count(EvaluationModel.id),
        func.avg(EvaluationModel.innovacion),
        func.avg(EvaluationModel.viabilidad),
        func.avg(EvaluationModel.presentacion),
        func.avg(EvaluationModel.general),
    ).where(EvaluationModel.proyecto_id == proyecto.id)

    total, innovacion, viabilidad, presentacion, general = (
        await session.execute(consulta)
    ).one()

    return Resumen(
        proyecto_id=proyecto.id,
        total_evaluaciones=total,
        innovacion=round(innovacion, 2) if innovacion is not None else None,
        viabilidad=round(viabilidad, 2) if viabilidad is not None else None,
        presentacion=round(presentacion, 2) if presentacion is not None else None,
        general=round(general, 2) if general is not None else None,
    )
