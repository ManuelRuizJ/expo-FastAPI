from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models import ProjectModel

SessionDep = Annotated[AsyncSession, Depends(get_session)]


async def buscar_proyecto(
    proyecto_id: int,
    session: SessionDep,
) -> ProjectModel:
    proyecto = await session.get(ProjectModel, proyecto_id)
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto
