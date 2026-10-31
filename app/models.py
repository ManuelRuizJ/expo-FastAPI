from sqlalchemy import ForeignKey, JSON, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ProjectModel(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    equipo: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    categoria: Mapped[str] = mapped_column(String(40), nullable=False)


class EvaluationModel(Base):
    __tablename__ = "evaluations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    proyecto_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    innovacion: Mapped[int] = mapped_column(Integer, nullable=False)
    viabilidad: Mapped[int] = mapped_column(Integer, nullable=False)
    presentacion: Mapped[int] = mapped_column(Integer, nullable=False)
    general: Mapped[int] = mapped_column(Integer, nullable=False)
