from sys import prefix
from typing import List

from fastapi import APIRouter, HTTPException
# pyrefly: ignore [missing-import]
from fastapi.params import Depends, Path

from database import get_db
from schemas import UsuarioRead
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from services.usuario_service import listar_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario, obtener_usuario_por_id
from schemas import UsuarioRead, UsuarioUpdate, UsuarioCreate

router = APIRouter(
    prefix = "/api/usuarios",
    tags = ["usuarios"]
)

@router.get("/",response_model=List[UsuarioRead])
def Obtener_usuarios(db: Session = Depends(get_db)):
    """
    Endpoint para obtener todos los registros de usuarios
    """
    usuarios = listar_usuarios(db)
    return usuarios

@router.post("/", response_model=UsuarioRead, status_code = 201)
def crear_usuario_endpoint(datos: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Endpoint para crear usuario
    """
    nuevo_usuario = crear_usuario(db, datos)
    return nuevo_usuario

@router.get("/{id}",response_model=UsuarioRead)
def obtener_usuario_endpoint(
        id: int = Path(...,gt=0, description="id del usuario a consultar"),
        db: Session = Depends(get_db)
):
    """
    Devuelve un usuario específico según su id
    """
    usuario = obtener_usuario_por_id(db, id)
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado")
    return usuario

@router.put("/{id}",response_model=UsuarioRead, status_code = 200)
def actualizar_usuario_endpoint(
        id: int = Path(...,gt=0, description="id del usuario a actualizar"),
        datos: UsuarioUpdate = None,
        db: Session = Depends(get_db)
):
    """
    Actualizar un usuario existente
    """

    usuario_actualizado = actualizar_usuario(db, id, datos)
    if not usuario_actualizado:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario con id {id} no encontrado"
        )
    return usuario_actualizado

@router.delete("/{id}", status_code = 204)
def eliminar_usuario_endpoint(
        id: int = Path(...,gt=0, description="id del usuario a eliminar"),
        db: Session = Depends(get_db)
):
    """
    Elimiina un Usuario por su ID
    """
    resultado = eliminar_usuario(db, id)
    if not resultado:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario con id {id} no encontrado"
        )
    return None