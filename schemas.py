# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field
from typing import Optional



class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1,max_length=255, description="Nombre de usuario")
#    contrasenha: str = Field(..., min_length=1,max_length=255, description="Contrasena de usuario")
    email: str = Field(..., min_length=1,max_length=255, description="Email de usuario")

class UsuarioCreate(UsuarioBase):
    """
    Esquema para crear un usuario
    """
    pass
class UsuarioUpdate(UsuarioBase):
    """
    Esquema para actualizar un usuario
    Permite que algunos campos sean opcionales
    """

    nombre: Optional[str] = Field(None, min_length = 1)
#    contrasenha: Optional[str] = Field(None, min_length = 1)
    email: Optional[str] = Field(None, min_length = 1)
    pass

class UsuarioRead(BaseModel):
    """"
    Esquema para las respuestas del API.
    Incluye el ID del Usuario
    """
    id: int
    nombre: str
#    contrasenha: str
    email: str
    model_config = {
        "from_attributes": True
    }