import asyncio
import time
import httpx

BASE = "http://127.0.0.1:8000/"

async def disparar(ruta):
    async with httpx.AsyncClient(timeout=30) as c:
        t0 = time.perf_counter()
        tareas = [c.get(BASE + ruta) for _ in range(5)]
        await asyncio.gather(*tareas)
        print(ruta, round(time.perf_counter() - t0, 1))

for ruta in["demo/bloqueante", "demo/async", "demo/sync"]:
    asyncio.run(disparar(ruta))