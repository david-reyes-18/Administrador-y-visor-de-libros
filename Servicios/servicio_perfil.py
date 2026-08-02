from Modelos.usuario import Usuario


class ServicioPerfil:

    def __init__(self, repositorio_usuarios):
        self.repositorio_usuarios = repositorio_usuarios

    def actualizar(self, usuario_actual: Usuario, nombre: str, apellido: str, correo: str, contrasena_actual: str = "", nueva_contrasena: str = "") -> Usuario:
        if usuario_actual is None:
            raise ValueError("No hay un usuario con sesión iniciada.")

        nombre = nombre.strip()
        apellido = apellido.strip()
        correo = correo.strip().lower()

        if not all((nombre, apellido, correo)):
            raise ValueError("Debes completar nombre, apellido y correo.")

        usuario_con_correo = self.repositorio_usuarios.buscar_por_correo(correo)

        if usuario_con_correo is not None and usuario_con_correo.id != usuario_actual.id:
            raise ValueError("El correo ya está registrado por otro usuario.")

        if contrasena_actual and not nueva_contrasena:
            raise ValueError("Debes ingresar una nueva contraseña.")

        if nueva_contrasena and not contrasena_actual:
            raise ValueError("Debes ingresar tu contraseña actual.")

        if nueva_contrasena and contrasena_actual != usuario_actual.contrasena:
            raise ValueError("La contraseña actual es incorrecta.")

        contrasena = nueva_contrasena if nueva_contrasena else usuario_actual.contrasena
        usuario_actualizado = Usuario(nombre=nombre, apellido=apellido, correo=correo, contrasena=contrasena, libros=usuario_actual.libros, id=usuario_actual.id)

        self.repositorio_usuarios.actualizar(usuario_actualizado)

        return usuario_actualizado
