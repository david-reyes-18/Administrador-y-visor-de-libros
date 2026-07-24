import re
from .baseval import Validador


class ValidadorNombre(Validador):

    @staticmethod
    def validar(valor: str) -> str:
        valor = valor.strip().title()

        if not valor.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras")

        return valor

class ValidadorCorreo(Validador):

    @staticmethod
    def validar(valor: str) -> str:
        correo = str(valor or "").strip().lower()

        if not re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",correo):
            raise ValueError("Correo inválido. Usa un formato como nombre@correo.com.")

        return correo

class ValidadorContrasena(Validador):

    @staticmethod
    def validar(valor: str) -> str:

        if len(valor) < 6:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

        return valor
