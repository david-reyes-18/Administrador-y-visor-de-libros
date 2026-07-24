from dataclasses import dataclass, field
from uuid import uuid4
from VALIDADORES.usuariovalido import ValidadorContrasena, ValidadorCorreo, ValidadorNombre

@dataclass
class Usuario:
    nombre: str
    apellido: str
    correo: str
    contrasena: str
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        self.nombre = ValidadorNombre.validar(self.nombre)
        self.apellido = ValidadorNombre.validar(self.apellido)
        self.correo = ValidadorCorreo.validar(self.correo)
        self.contrasena = ValidadorContrasena.validar(self.contrasena)