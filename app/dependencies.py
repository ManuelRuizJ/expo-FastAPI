from fastapi import HTTPException

from app.repository import repositorio
from app.schemas import Proyecto

def buscar_proyecto(proyecto_id: int) -> Proyecto:
    proyecto = repositorio.obtener_proyecto(proyecto_id)
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto