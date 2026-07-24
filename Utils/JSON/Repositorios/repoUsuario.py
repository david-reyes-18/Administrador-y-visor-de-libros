from dataclasses import asdict

from ...RUTAS.rutas import RUTA_USUARIOS
from Modelos.usuario import Usuario
from .repoJSON import cargar_json, guardar_json


class RepositorioUsuario:

    def obtener_todos(self) -> list[Usuario]:
        datos = cargar_json(RUTA_USUARIOS)

        return [
            Usuario(**usuario)
            for usuario in datos
        ]

    def buscar_por_correo(self, correo: str) -> Usuario | None:
        correo = correo.strip().lower()

        for usuario in self.obtener_todos():
            if usuario.correo == correo:
                return usuario

        return None

    def agregar(self, usuario: Usuario) -> None:
        if self.buscar_por_correo(usuario.correo):
            raise ValueError("El correo ya está registrado")

        usuarios = self.obtener_todos()
        usuarios.append(usuario)

        datos = [
            asdict(usuario)
            for usuario in usuarios
        ]

        guardar_json(RUTA_USUARIOS, datos)