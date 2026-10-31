import logging
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, status
from sqlalchemy import select

from app.dependencies import SessionDep, buscar_proyecto
from app.models import EvaluationModel, ProjectModel
from app.schemas import Evaluacion, EvaluacionIn

router = APIRouter(
    prefix="/proyectos/{proyecto_id}/evaluaciones",
    tags=["Evaluaciones"],
)

logger = logging.getLogger(__name__)


def registrar_evaluacion(evaluacion_id: int, proyecto_id: int) -> None:
    # Ejemplo didáctico de tarea en segundo plano.
    logger.info(
        "Evaluación %s registrada para el proyecto %s",
        evaluacion_id,
        proyecto_id,
    )


@router.post("", response_model=Evaluacion, status_code=status.HTTP_201_CREATED)
async def crear_evaluacion(
    proyecto: Annotated[ProjectModel, Depends(buscar_proyecto)],
    datos: EvaluacionIn,
    session: SessionDep,
    background_tasks: BackgroundTasks,
):
    evaluacion = EvaluationModel(
        proyecto_id=proyecto.id,
        **datos.model_dump(),
    )
    session.add(evaluacion)
    await session.commit()
    await session.refresh(evaluacion)

    background_tasks.add_task(
        registrar_evaluacion,
        evaluacion.id,
        proyecto.id,
    )
    return evaluacion


@router.get("", response_model=list[Evaluacion])
async def listar_evaluaciones(
    proyecto: Annotated[ProjectModel, Depends(buscar_proyecto)],
    session: SessionDep,
):
    consulta = (
        select(EvaluationModel)
        .where(EvaluationModel.proyecto_id == proyecto.id)
        .order_by(EvaluationModel.id)
    )
    resultado = await session.execute(consulta)
    return resultado.scalars().all()
