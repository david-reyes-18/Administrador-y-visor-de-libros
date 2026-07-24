from Modelos.usuario import Usuario


class ServicioRegistro:

    def __init__(self, repositorio_usuarios):
        self.repositorio_usuarios = repositorio_usuarios

    def registrar(self, nombre: str, apellido: str, correo: str, contrasena: str, confirmacion: str) -> Usuario:
        nombre = nombre.strip()
        apellido = apellido.strip()
        correo = correo.strip().lower()

        if not all((nombre, apellido, correo, contrasena, confirmacion)):
            raise ValueError("Debes completar todos los campos.")

        if contrasena != confirmacion:
            raise ValueError("Las contraseñas no coinciden.")

        usuario = Usuario(nombre=nombre, apellido= apellido, correo=correo, contrasena=contrasena)
        self.repositorio_usuarios.agregar(usuario)

        return usuario