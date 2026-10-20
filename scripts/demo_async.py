import asyncio
import time
from fastapi import FastAPI


app = FastAPI()


@app.get("/demo/bloqueante")
async def bloqueante():
    time.sleep(2)
    return {"tipo:" "async def + time.sleep"}


@app.get("/demo/async")
async def asincrono():
    await asyncio.sleep(2)
    return {"tipo:" "async def + await async.sleep"}


@app.get("/demo/sync")
async def sincrono():
    time.sleep(2)
    return {"tipo:" "async def + sleep"}
