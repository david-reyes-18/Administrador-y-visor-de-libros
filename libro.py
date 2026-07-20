from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Libro:
    titulo: str
    autor: str
    año_publi: int
    id: str = field(default_factory=lambda: str(uuid4()))
    leido: bool = False

    def marcar_leido(self) -> None:
        self.leido = True
