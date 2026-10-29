from fastapi import FastAPI, APIRouter
from app.routers import projects, evaluations

app = FastAPI(title="Mini Evaluación Expo Ibero")

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(router=projects.router)
api_v1.include_router(router=evaluations.router)

app.include_router(router=api_v1)

@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo desde FASTAPI :)"}
