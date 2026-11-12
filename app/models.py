from sqlalchemy import JSON, Column
from sqlmodel import Field, Relationship, SQLModel

from app.schemas import Categoria

class ProyectoDB(SQLModel, table=True):
    __tablename__ = "proyectos"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=120, unique=True, index=True)
    equipo: list[str] = Field(sa_column=Column(JSON, nullable=False))
    categoria : Categoria

    evaluaciones: list["EvaluacionesDB"] = Relationship(
        back_populates="proyecto", cascade_delete=True
    )


class EvaluacionesDB(SQLModel, table=True):
    __tablename__ = "evaluaciones"

    id: int | None = Field(default=None, primary_key=True)
    proyecto_id: int = Field(foreign_key="proyectos.id", index=True, ondelete="CASCADE")
    evaluador: str = Field(max_length=80)
    innovacion: int
    viabilidad: int
    presentacion: int
    comentarios: str | None = Field(default=None, max_length=300)

    proyecto: ProyectoDB | None = Relationship(back_populates="evaluaciones")