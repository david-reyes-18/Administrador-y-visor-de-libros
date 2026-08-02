import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from Utils.utils import BEIGE_MADERA, CREMA_TEXTO, GRIS, GRIS_BORDE, MARRON_MADERA, MARRON_OSCURO, NEGRO_PANEL
from presentacion.vistas.vista_base import VistaBase


class VistaPerfil(ctk.CTkFrame, VistaBase):

    def __init__(self, padre, navegacion):
        super().__init__(padre, fg_color=NEGRO_PANEL, corner_radius=15, border_width=1, border_color=GRIS_BORDE)
        self.navegacion = navegacion
        self.usuario = self.navegacion.master.usuario_actual
        self.crear_interfaz()

    def crear_interfaz(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        nombre = getattr(self.usuario, "nombre", "Nombre")
        apellido = getattr(self.usuario, "apellido", "Apellido")
        correo = getattr(self.usuario, "correo", "correo@ejemplo.com")
        total_libros = len(getattr(self.usuario, "libros", []))

        encabezado = ctk.CTkFrame(self, fg_color="transparent")
        encabezado.grid(row=0, column=0, sticky="ew", padx=30, pady=(25, 15))

        titulo = ctk.CTkLabel(encabezado, text="Mi perfil", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=28, weight="bold"))
        titulo.pack(anchor="w")

        descripcion = ctk.CTkLabel(encabezado, text="Consulta y administra la información de tu cuenta.", text_color=BEIGE_MADERA, font=ctk.CTkFont(size=15))
        descripcion.pack(anchor="w", pady=(4, 0))

        cuerpo = ctk.CTkFrame(self, fg_color="transparent")
        cuerpo.grid(row=1, column=0, sticky="nsew", padx=30, pady=(0, 30))
        cuerpo.grid_columnconfigure(0, weight=0, minsize=220)
        cuerpo.grid_columnconfigure(1, weight=1)
        cuerpo.grid_rowconfigure(0, weight=1)

        tarjeta_usuario = ctk.CTkFrame(cuerpo, width=220, corner_radius=15, fg_color=MARRON_OSCURO, border_width=1, border_color=GRIS_BORDE)
        tarjeta_usuario.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        tarjeta_usuario.grid_propagate(False)

        avatar = ctk.CTkFrame(tarjeta_usuario, width=110, height=110, corner_radius=55, fg_color=MARRON_MADERA, border_width=2, border_color=BEIGE_MADERA)
        avatar.pack(pady=(35, 15))
        avatar.pack_propagate(False)

        icono = ctk.CTkLabel(avatar, text="👤", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=50))
        icono.pack(expand=True)

        self.nombre_usuario = ctk.CTkLabel(tarjeta_usuario, text=f"{nombre} {apellido}", wraplength=190, text_color=CREMA_TEXTO, font=ctk.CTkFont(size=19, weight="bold"))
        self.nombre_usuario.pack(padx=15)

        self.correo_usuario = ctk.CTkLabel(tarjeta_usuario, text=correo, wraplength=190, text_color=BEIGE_MADERA, font=ctk.CTkFont(size=13))
        self.correo_usuario.pack(padx=15, pady=(5, 25))

        separador = ctk.CTkFrame(tarjeta_usuario, height=1, fg_color=GRIS_BORDE)
        separador.pack(fill="x", padx=20, pady=(0, 20))

        estadistica_libros = ctk.CTkLabel(tarjeta_usuario, text=f"{total_libros}   Libros guardados", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=15, weight="bold"))
        estadistica_libros.pack(anchor="w", padx=25, pady=7)

        estadistica_lectura = ctk.CTkLabel(tarjeta_usuario, text="0   En lectura", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=15, weight="bold"))
        estadistica_lectura.pack(anchor="w", padx=25, pady=7)

        estadistica_terminados = ctk.CTkLabel(tarjeta_usuario, text="0   Terminados", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=15, weight="bold"))
        estadistica_terminados.pack(anchor="w", padx=25, pady=7)

        formulario = ctk.CTkFrame(cuerpo, corner_radius=15, fg_color=MARRON_OSCURO, border_width=1, border_color=GRIS_BORDE)
        formulario.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        formulario.grid_columnconfigure((0, 1), weight=1)

        titulo_formulario = ctk.CTkLabel(formulario, text="Información personal", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=20, weight="bold"))
        titulo_formulario.grid(row=0, column=0, columnspan=2, sticky="w", padx=25, pady=(25, 20))

        etiqueta_nombre = ctk.CTkLabel(formulario, text="Nombre", text_color=BEIGE_MADERA, font=ctk.CTkFont(size=13))
        etiqueta_nombre.grid(row=1, column=0, sticky="w", padx=(25, 10), pady=(0, 5))

        etiqueta_apellido = ctk.CTkLabel(formulario, text="Apellido", text_color=BEIGE_MADERA, font=ctk.CTkFont(size=13))
        etiqueta_apellido.grid(row=1, column=1, sticky="w", padx=(10, 25), pady=(0, 5))

        self.entrada_nombre = ctk.CTkEntry(formulario, height=42, fg_color=NEGRO_PANEL, border_color=GRIS_BORDE, text_color=CREMA_TEXTO)
        self.entrada_nombre.grid(row=2, column=0, sticky="ew", padx=(25, 10), pady=(0, 15))
        self.entrada_nombre.insert(0, nombre)

        self.entrada_apellido = ctk.CTkEntry(formulario, height=42, fg_color=NEGRO_PANEL, border_color=GRIS_BORDE, text_color=CREMA_TEXTO)
        self.entrada_apellido.grid(row=2, column=1, sticky="ew", padx=(10, 25), pady=(0, 15))
        self.entrada_apellido.insert(0, apellido)

        etiqueta_correo = ctk.CTkLabel(formulario, text="Correo electrónico", text_color=BEIGE_MADERA, font=ctk.CTkFont(size=13))
        etiqueta_correo.grid(row=3, column=0, columnspan=2, sticky="w", padx=25, pady=(0, 5))

        self.entrada_correo = ctk.CTkEntry(formulario, height=42, fg_color=NEGRO_PANEL, border_color=GRIS_BORDE, text_color=CREMA_TEXTO)
        self.entrada_correo.grid(row=4, column=0, columnspan=2, sticky="ew", padx=25, pady=(0, 15))
        self.entrada_correo.insert(0, correo)

        etiqueta_contrasena_actual = ctk.CTkLabel(formulario, text="Contraseña actual", text_color=BEIGE_MADERA, font=ctk.CTkFont(size=13))
        etiqueta_contrasena_actual.grid(row=5, column=0, columnspan=2, sticky="w", padx=25, pady=(0, 5))

        self.entrada_contrasena_actual = ctk.CTkEntry(formulario, height=42, placeholder_text="Ingresa tu contraseña actual", show="*", fg_color=NEGRO_PANEL, border_color=GRIS_BORDE, text_color=CREMA_TEXTO)
        self.entrada_contrasena_actual.grid(row=6, column=0, columnspan=2, sticky="ew", padx=25, pady=(0, 15))

        etiqueta_nueva_contrasena = ctk.CTkLabel(formulario, text="Nueva contraseña", text_color=BEIGE_MADERA, font=ctk.CTkFont(size=13))
        etiqueta_nueva_contrasena.grid(row=7, column=0, columnspan=2, sticky="w", padx=25, pady=(0, 5))

        self.entrada_nueva_contrasena = ctk.CTkEntry(formulario, height=42, placeholder_text="Dejar ambos campos vacíos para mantenerla", show="*", fg_color=NEGRO_PANEL, border_color=GRIS_BORDE, text_color=CREMA_TEXTO)
        self.entrada_nueva_contrasena.grid(row=8, column=0, columnspan=2, sticky="ew", padx=25, pady=(0, 20))

        botones = ctk.CTkFrame(formulario, fg_color="transparent")
        botones.grid(row=9, column=0, columnspan=2, sticky="e", padx=25, pady=(10, 25))

        boton_restablecer = ctk.CTkButton(botones, text="Restablecer", width=110, fg_color="transparent", border_width=1, border_color=GRIS, hover_color=GRIS_BORDE, text_color=CREMA_TEXTO, command=self.restablecer_campos)
        boton_restablecer.pack(side="left", padx=(0, 10))

        boton_guardar = ctk.CTkButton(botones, text="Guardar cambios", width=140, fg_color=MARRON_MADERA, hover_color=BEIGE_MADERA, text_color=CREMA_TEXTO, command=self.guardar_cambios)
        boton_guardar.pack(side="left")

    def guardar_cambios(self):
        try:
            usuario_actualizado = self.navegacion.master.servicio_perfil.actualizar(
                usuario_actual=self.usuario,
                nombre=self.entrada_nombre.get(),
                apellido=self.entrada_apellido.get(),
                correo=self.entrada_correo.get(),
                contrasena_actual=self.entrada_contrasena_actual.get(),
                nueva_contrasena=self.entrada_nueva_contrasena.get()
            )

        except ValueError as error:
            CTkMessagebox(title="Perfil", message=str(error), icon="cancel")
            return

        self.usuario = usuario_actualizado
        self.navegacion.master.usuario_actual = usuario_actualizado
        self.nombre_usuario.configure(text=f"{usuario_actualizado.nombre} {usuario_actualizado.apellido}")
        self.correo_usuario.configure(text=usuario_actualizado.correo)
        self.entrada_contrasena_actual.delete(0, "end")
        self.entrada_nueva_contrasena.delete(0, "end")
        CTkMessagebox(title="Perfil", message="El perfil fue actualizado correctamente.", icon="check")

    def restablecer_campos(self):
        self.entrada_nombre.delete(0, "end")
        self.entrada_nombre.insert(0, self.usuario.nombre)
        self.entrada_apellido.delete(0, "end")
        self.entrada_apellido.insert(0, self.usuario.apellido)
        self.entrada_correo.delete(0, "end")
        self.entrada_correo.insert(0, self.usuario.correo)
        self.entrada_contrasena_actual.delete(0, "end")
        self.entrada_nueva_contrasena.delete(0, "end")
