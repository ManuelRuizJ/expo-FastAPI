import logging
from contextlib import asynccontextmanager
from time import perf_counter

from fastapi import APIRouter, FastAPI, Request

from app.config import get_settings
from app.database import close_database, create_database
from app.routers import evaluations, projects

settings = get_settings()
logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield
    await close_database()


app = FastAPI(title=settings.app_name, lifespan=lifespan)


@app.middleware("http")
async def medir_tiempo_respuesta(request: Request, call_next):
    inicio = perf_counter()
    response = await call_next(request)
    duracion = perf_counter() - inicio
    response.headers["X-Process-Time"] = f"{duracion:.6f}"
    return response


api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(projects.router)
api_v1.include_router(evaluations.router)
app.include_router(api_v1)


@app.get("/")
async def raiz():
    return {"mensaje": "Hola mundo desde FastAPI"}
