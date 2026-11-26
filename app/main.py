from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse
from app.routers import projects, evaluations
from app.database import crear_tablas
from app.errors import Conflicto

@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield

app = FastAPI(title="Mini Evaluación Expo Ibero", lifespan=lifespan)


@app.exception_handler(Conflicto)
def manejar_conflicto(request: Request, exc: Conflicto):
    return JSONResponse(status_code=409, content={"detail": exc.mensaje})

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(router=projects.router)
api_v1.include_router(router=evaluations.router)

app.include_router(router=api_v1)

@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo desde FASTAPI :)"}