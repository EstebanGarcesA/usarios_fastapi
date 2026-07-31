from fastapi import FastAPI
from api.usuarios import router as usuarios_router

app = FastAPI()


@app.get("/")
async def inicio():
    return {"message": "La Api de usuarios esta funcionando"}

app.include_router(usuarios_router)

