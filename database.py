import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# ==========================================================
# Cargar las variables del archivo .env
# ==========================================================
load_dotenv()


# ==========================================================
# Obtener los datos de conexión desde las variables
# de entorno.
# ==========================================================
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# ==========================================================
# Construcción de la URL de conexión utilizando PyMySQL.
# ==========================================================
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# ==========================================================
# Engine
#
# Es el encargado de administrar la comunicación con
# la base de datos.
# ==========================================================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# ==========================================================
# SessionLocal
#
# Fabrica de sesiones que utilizará la aplicación para
# realizar operaciones sobre la base de datos.
# ==========================================================
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


# ==========================================================
# Base
#
# Todos los modelos de SQLAlchemy heredarán de esta clase.
# ==========================================================
Base = declarative_base()


# ==========================================================
# Dependencia para FastAPI
#
# Abre una sesión por petición y garantiza que siempre
# será cerrada al finalizar.
# ==========================================================
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ==========================================================
# Prueba de conexión
#
# Permite comprobar rápidamente que la conexión con
# MySQL funciona correctamente.
#
# Ejecutar:
#     python database.py
# ==========================================================
if __name__ == "__main__":
    try:
        with engine.connect():
            print("✅ Conexión con MySQL realizada correctamente.")
    except Exception as e:
        print("❌ Error al conectar con MySQL.")
        print(e)