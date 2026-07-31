from sqlalchemy.orm import Session

from models import usuario
from models.usuario import Usuario
from schemas import UsuarioCreate, UsuarioUpdate

def listar_usuarios(session: Session):
    """"
    Devuelve una lista con todos los usarios almacenados en la base de datos
    """
    return session.query(Usuario).all()

def crear_usuario(db: Session, usuario: Usuario):
    """
    Crea un nuevo usuario en la base de datos usando los datos validados del esquema LibroCreate
    """
    nuevo_usuario = Usuario(
        nombre =usuario.nombre,
        contrasenha= usuario.contrasenha,
        email = usuario.email
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def obtener_usuario_por_id(db: Session, id: int):
    """
    Obtiene un usuario por su ID
    """
    return db.query(usuario).filter(usuario.id == id).first()

def actualizar_usuario(db: Session, id: int, datos: UsuarioUpdate):
    """
    Actualiza un usuario existente solo se modifican los campos que el usuario envie
    """
    usuario = obtener_usuario_por_id(db, id)

    if not usuario:
        return None

    if datos.nombre is not None:
        usuario.nombre = datos.nombre
    if datos.contrasenha is not None:
        usuario.contrasenha = datos.contrasenha
    if datos.email is not None:
        usuario.email = datos.email
    db.commit()
    db.refresh(usuario)
    return usuario

def eliminar_usuario(db: Session, id: int):
    """
    Elimina un libro de la base de datos si existe
    """
    usuario = obtener_usuario_por_id(db, id)
    if not usuario:
        return None
    db.delete(usuario)
    db.commit()
    return True