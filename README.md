# Mini Evaluación Expo Ibero — FastAPI

API de práctica para las sesiones 14 y 15: routers modulares, middleware,
background tasks, configuración con Pydantic Settings e integración asíncrona
con SQLite mediante SQLAlchemy.

## Requisitos

- Python 3.11 o superior
- Un entorno virtual

## Instalación

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

En Windows, activa el entorno con `venv\\Scripts\\activate`.

## Ejecutar

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Ruta raíz: http://127.0.0.1:8000/

La base SQLite `expo_fastapi.db` se crea al iniciar la aplicación. Para este
ejercicio se usa `create_all`; en un proyecto real se deben gestionar los
cambios de esquema con Alembic.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/api/v1/proyectos` | Crear proyecto |
| GET | `/api/v1/proyectos` | Listar proyectos |
| GET | `/api/v1/proyectos/{id}` | Consultar proyecto |
| GET | `/api/v1/proyectos/{id}/resumen` | Resumen de evaluaciones |
| POST | `/api/v1/proyectos/{id}/evaluaciones` | Crear evaluación |
| GET | `/api/v1/proyectos/{id}/evaluaciones` | Listar evaluaciones |

## Ejemplos de JSON

Crear proyecto:

```json
{
  "nombre": "Sistema de evaluación",
  "equipo": ["Ana", "Luis"],
  "categoria": "Software"
}
```

Crear evaluación:

```json
{
  "innovacion": 5,
  "viabilidad": 4,
  "presentacion": 5,
  "general": 5
}
```

## ¿Qué se practica?

- **Routers:** endpoints separados por recurso.
- **Middleware:** agrega el encabezado `X-Process-Time` a las respuestas.
- **BackgroundTasks:** registra en el log la creación de una evaluación.
- **Pydantic Settings:** lee configuración desde variables de entorno y `.env`.
- **SQLAlchemy async:** modelos, motor, sesiones y consultas asíncronas.
- **CRUD:** creación y consulta de proyectos y evaluaciones.

> Nota: la tarea en segundo plano es un ejemplo sencillo ejecutado por el propio
> proceso de FastAPI; no sustituye una cola de trabajos como Celery.
