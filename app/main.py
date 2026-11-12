from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from app.routers import projects, evaluations
from app.database import crear_tablas

@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield

app = FastAPI(title="Mini Evaluación Expo Ibero", lifespan=lifespan)

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(router=projects.router)
api_v1.include_router(router=evaluations.router)

app.include_router(router=api_v1)

@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo desde FASTAPI :)"}