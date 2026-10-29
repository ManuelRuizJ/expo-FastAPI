from app.schemas import ProyectoIn, Proyecto, Categoria, Evaluacion, EvaluacionIn, Resumen

class RepositoryMemory:
    def __init__(self) -> None:
        self.proyecto: dict[int, Proyecto] = {}
        self.evaluacion: dict[int, Evaluacion] = {}
        self.siguiente_id = 1
        self.siguiente_evaluacion_id = 1

    # Proyectos
    def crear_proyecto(self, datos: ProyectoIn) -> Proyecto:
        proyecto = Proyecto(id = self.siguiente_id, **datos.models_dump())
        self.proyectos[proyecto.id] = Proyecto
        self.siguiente_id += 1
        return proyecto

    def listar_proyectos(self, categoria: Categoria | None, limite: int) -> list[Proyecto]:
        resultado = [
            p for p in self.proyecto.values()
            if categoria is None or p.categoria == categoria
        ]
        return resultado[:limite]

    def obtener_proyecto(self, proyecto_id: int) -> Proyecto | None:
        return self.proyectos.get(proyecto_id)

    # Evaluacion
    def crear_evaluacion(self, proyecto_id: int, datos: EvaluacionIn) -> Evaluacion:
        evaluacion = Evaluacion(
            id = self.siguiente_evaluacion_id,
            proyecto_id = proyecto_id,
            **datos.model_dump())
        self.evaluaciones[evaluacion.id] = evaluacion
        self.siguiente_evaluacion_id += 1
        return evaluacion

    def listar_evaluaciones(self, proyecto_id: int) -> list[Evaluacion]:
        return [e for e in self.evaluaciones.values() if e.proyecto_id == proyecto_id]

    def resumen(self, proyecto_id: int) -> Resumen: 
        del_proyecto = [e for e in self.evaluaciones.values() if e.proyecto_id == proyecto_id]
        total = len(del_proyecto)
        if total == 0:
            return Resumen(
                proyecto_id = proyecto_id, total_evaluaciones = 0,
                innovacion = None, vabilidad = None, presentacion = None, general = None
            )

        innovacion = sum(e.innovacion for e in del_proyecto) / total
        vabilidad = sum(e.viabilidad for e in del_proyecto) / total
        presentacion = sum(e.presentacion for e in del_proyecto) / total
        general = sum(e.general for e in del_proyecto) / total
        return Resumen(
            proyecto_id = proyecto_id, 
            total_evaluaciones = total,
            innovacion = round(innovacion, 2),
            vabilidad = round(vabilidad, 2),
            presentacion = round(presentacion, 2),
            general = round(general, 2)
        )

        


repositorio = RepositoryMemory()