from fastapi import FastAPI
from api.usuarios import router as usuarios_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
 "http://localhost:5173", # React Vite
] #
app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)


@app.get("/")
async def inicio():
    return {"message": "La Api de usuarios esta funcionando"}

app.include_router(usuarios_router)

