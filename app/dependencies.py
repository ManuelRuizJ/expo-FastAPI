from typing import Annotated

from fastapi import Depends, HTTPException

from app.database import SessionDep
from app.models import ProyectoDB
from app.repository_sql import RepositorySQL


def get_repositorio(session: SessionDep) -> RepositorySQL:
    return RepositorySQL(session)


RepositorioDep = Annotated[RepositorySQL, Depends(get_repositorio)]


def buscar_proyecto(proyecto_id: int, repositorio: RepositorioDep) -> ProyectoDB:
    proyecto = repositorio.obtener_proyecto(proyecto_id)
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


ProyectoDep = Annotated[ProyectoDB, Depends(buscar_proyecto)]
