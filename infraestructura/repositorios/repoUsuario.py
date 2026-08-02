from dataclasses import asdict

from infraestructura.manejador_jsons.manejador_jsons import ManejadorJSON
from infraestructura.manejador_rutas.rutas import Rutas
from Modelos.usuario import Usuario


class RepositorioUsuario:

    def obtener_todos(self) -> list[Usuario]:
        datos = ManejadorJSON.cargar_json(Rutas.get_json("usuarios.json"))

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

        ManejadorJSON.guardar_json(Rutas.get_json("usuarios.json"), datos)

    def actualizar(self, usuario_actualizado: Usuario) -> None:
        usuarios = self.obtener_todos()

        for indice, usuario in enumerate(usuarios):
            if usuario.id == usuario_actualizado.id:
                usuarios[indice] = usuario_actualizado
                break
        else:
            raise ValueError("El usuario no existe.")

        datos = [
            asdict(usuario)
            for usuario in usuarios
        ]

        ManejadorJSON.guardar_json(Rutas.get_json("usuarios.json"), datos)
