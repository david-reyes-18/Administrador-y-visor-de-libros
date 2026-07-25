import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from infraestructura.manejador_rutas.rutas import Rutas
from Utils.utils import BEIGE_MADERA, MARRON_MADERA, crear_imagen_fondo
from presentacion.navegacion.tipo_vista import TipoVista
from presentacion.vistas.vista_base import VistaBase


class VistaLogin(ctk.CTkFrame, VistaBase):
    
    def __init__(self, padre, navegacion):
        super().__init__(padre)

        self.imagen_fondo = crear_imagen_fondo()
        self.fondo = ctk.CTkLabel(self, text="", image=self.imagen_fondo)
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.ajustar_fondo)

        self.navegacion = navegacion
        self.crear_interfaz()

    def ajustar_fondo(self, evento):
        if evento.width > 1 and evento.height > 1:
            self.imagen_fondo.configure(size=(evento.width, evento.height))

    def crear_interfaz(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        formulario = ctk.CTkFrame(self, width=400, height=450, corner_radius=20)
        formulario.grid(row=0, column=0, padx=20, pady=20)

        formulario.grid_propagate(False)
        formulario.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(formulario, text="Iniciar sesión", font=("Arial", 30, "bold"))
        titulo.grid(row=0, column=0, padx=5, pady=(50, 30))

        self.entrada_correo = ctk.CTkEntry( formulario, width=300, height=45, placeholder_text="Correo")
        self.entrada_correo.grid(row=1, column=0, padx=40, pady=10)

        self.entrada_contrasena = ctk.CTkEntry(formulario, width=300, height=45, placeholder_text="Contraseña", show="*")
        self.entrada_contrasena.grid(row=2, column=0, padx=40, pady=10)

        boton_ingresar = ctk.CTkButton(formulario, text="Ingresar", width=300, height=45, fg_color = MARRON_MADERA, hover_color = BEIGE_MADERA, command=self.iniciar_sesion)
        boton_ingresar.grid(row=3, column=0, padx=40, pady=(30, 10))

        boton_registro = ctk.CTkButton(formulario, text="Crear cuenta", width=300, height=45, fg_color="transparent", border_width=1, hover_color = BEIGE_MADERA,  border_color=MARRON_MADERA, text_color=BEIGE_MADERA, command=lambda: self.navegacion.mostrar_vista(TipoVista.REGISTRO))
        boton_registro.grid(row=4, column=0, padx=40, pady=10)

    def iniciar_sesion(self):
        try:
            usuario = self.navegacion.master.servicio_login.autenticar(correo=self.entrada_correo.get(), contrasena=self.entrada_contrasena.get())

        except ValueError as error:
            CTkMessagebox(title="Inicio de sesión", message=str(error), icon="cancel")
            return

        self.navegacion.master.usuario_actual = usuario
        CTkMessagebox(title="Inicio de sesión", message="Sesión iniciada correctamente.", icon="check")
