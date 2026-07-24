import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from Utils.utils import *

class VistaRegistro(ctk.CTkFrame):

    def __init__(self, padre, navegacion):
        super().__init__(padre)

        fondo = ctk.CTkLabel(self, text="", image=IMG_FONDO)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.navegacion = navegacion
        self.crear_interfaz()

    def crear_interfaz(self):
        self.grid_columnconfigure(0, weight=3)
        self.grid_rowconfigure(0, weight=2)

        formulario = ctk.CTkFrame(self, width=950, height=600, corner_radius=20)
        formulario.grid(row=0, column=0, padx=30, pady=30)

        formulario.grid_propagate(False)
        formulario.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(formulario, text="Registro", font=("Arial", 30, "bold"))
        titulo.grid(row=0, column=0, padx=(130, 0), pady=(25, 18), sticky="w")

        imagen_troll = ctk.CTkLabel(formulario, text="", image= BRR_PATAPIMES)
        imagen_troll.grid(row=0, column=1, rowspan=8, padx=(20, 50), pady=30, sticky="e")

        self.entrada_nombre = ctk.CTkEntry(formulario, width=300,  height=45, placeholder_text="Nombre")
        self.entrada_nombre.grid(row=1, column=0, padx=40, pady=10, sticky="w")

        self.entrada_apellido = ctk.CTkEntry(formulario, width=300,  height=45, placeholder_text="Apellido")
        self.entrada_apellido.grid(row=2, column=0, padx=40, pady=10, sticky="w")

        self.entrada_correo = ctk.CTkEntry(formulario, width=300, height=45, placeholder_text="Correo")
        self.entrada_correo.grid(row=3, column=0, padx=40, pady=10, sticky="w")

        self.entrada_contrasena = ctk.CTkEntry(formulario, width=300, height=45, placeholder_text="Contraseña", show="*")
        self.entrada_contrasena.grid(row=4, column=0, padx=40, pady=10, sticky="w")

        self.entrada_confirmacion = ctk.CTkEntry(formulario, width=300, height=45, placeholder_text="Confirmar contraseña", show="*")
        self.entrada_confirmacion.grid(row=5, column=0, padx=40, pady=10, sticky="w")

        boton_registro = ctk.CTkButton(formulario, text="Crear cuenta", width=300, height=45, fg_color=MARRON_MADERA, border_width=1, hover_color = BEIGE_MADERA, command=lambda: self.registrar())
        boton_registro.grid(row=6, column=0, padx=40, pady=10, sticky="w")

        boton_volver = ctk.CTkButton(formulario, text="Volver al inicio de sesión", width=300, height=45, fg_color="transparent", hover_color=BEIGE_MADERA, border_width=1, border_color=MARRON_MADERA, text_color=BEIGE_MADERA, command=lambda: self.navegacion.navegar("login"))
        boton_volver.grid(row=7, column=0, padx=40, pady=10, sticky="w")


    def registrar(self):
        try:
            self.navegacion.servicio_registro.registrar(
                nombre=self.entrada_nombre.get(),
                apellido = self.entrada_apellido.get(),
                correo=self.entrada_correo.get(),
                contrasena=self.entrada_contrasena.get(),
                confirmacion=self.entrada_confirmacion.get()
            )

        except ValueError as error:
            CTkMessagebox(title="Registro", message=str(error), icon="cancel")
            return

        CTkMessagebox( title="Registro exitoso", message="La cuenta fue creada correctamente.", icon="check")
        self.navegacion.navegacion("aqui falta xd")
