class ServicioInicioSesion:

    def __init__(self, repositorio_usuarios):
        self.repositorio_usuarios = repositorio_usuarios

    def autenticar(self, correo: str, contrasena: str):
        correo = correo.strip().lower()

        if not correo or not contrasena:
            raise ValueError("Debes completar todos los campos.")

        usuario = self.repositorio_usuarios.buscar_por_correo(correo)

        if usuario is None or usuario.contrasena != contrasena:
            raise ValueError("Correo o contraseña incorrectos.")

        return usuario