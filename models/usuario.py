from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from database import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)

    nombre = Column(String(255),nullable=False )

    contrasenha = Column(String(255),nullable=False)

    email = Column(String(255),nullable=False)

 #   fecha_registro = Column(DateTime,nullable=False)

