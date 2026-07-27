import customtkinter as ctk
from Utils.utils import *
from presentacion.vistas.vista_base import VistaBase
from presentacion.navegacion.tipo_vista import TipoVista

class Menu(ctk.CTkFrame, VistaBase):
    
    def __init__(self, padre, navegacion):
        super().__init__(padre, fg_color=NEGRO_FONDO)

        self.menu_expandido = True
        self.navegacion = navegacion
        self.crear_interfaz()

    def crear_interfaz(self):
        self.grid_columnconfigure(0, weight=0, minsize=260)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.cabecera = ctk.CTkFrame(self, width=500, height=100, corner_radius=20, fg_color=NEGRO_PANEL, border_width=1, border_color=GRIS_BORDE)
        self.cabecera.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(20, 5))
        self.cabecera.grid_propagate(False)

        self.bob_esponja = ctk.CTkLabel(self.cabecera, text="", image= BOB_ESPONJA)
        self.bob_esponja.place(relx=0.5, rely=0.5, x=-180, anchor="center")

        self.titulo = ctk.CTkLabel(self.cabecera, text="Libreria Tung Tung", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=28, weight="bold"))
        self.titulo.pack(padx=30, pady=20)

        self.menu_scroll = ctk.CTkScrollableFrame(self, width=230, corner_radius=15, fg_color=MARRON_OSCURO, border_width=1, border_color=GRIS_BORDE, scrollbar_button_color=GRIS_BORDE, scrollbar_button_hover_color=GRIS)
        self.menu_scroll.grid(row=1, column=0, sticky="nsew", padx=(20, 5), pady=(10, 20))
        self.menu_scroll.grid_columnconfigure(0, weight=1)

        self.boton_menu = ctk.CTkButton(self.menu_scroll, text="☰", width=50, height=45, corner_radius=10, fg_color=MARRON_MADERA, hover_color=BEIGE_MADERA, text_color=CREMA_TEXTO, command=self.alternar_menu)
        self.boton_menu.grid(row=0, column=0, sticky="ew", padx=10, pady=(8, 4))

        self.boton_cerrar_sesion = ctk.CTkButton(self.cabecera, text="Cerrar sesión", width=125, height=36, corner_radius=10, fg_color=ROJO_ACENTO, hover_color=ROJO_HOVER, text_color=CREMA_TEXTO, command=lambda: self.navegacion.mostrar_vista(TipoVista.LOGIN))
        self.boton_cerrar_sesion.place(relx=1.0, rely=0.5, x=-20, anchor="e")

        self.boton_inicio = ctk.CTkButton(self.menu_scroll, text="🏠  Inicio", height=60, corner_radius=10, fg_color=MARRON_MADERA, hover_color=BEIGE_MADERA, text_color=CREMA_TEXTO, anchor="w", command=self.accion_boton)
        self.boton_inicio.grid(row=1, column=0, sticky="ew", padx=10, pady=8)

    def alternar_menu(self):
        if self.menu_expandido:
            self.cerrar_menu()
        else:
            self.abrir_menu()

    def cerrar_menu(self):
        self.menu_expandido = False

        self.grid_columnconfigure(0, minsize= ANCHO_MENU_CERRADO)
        self.menu_scroll.configure(width= ANCHO_MENU_CERRADO)

        self.boton_inicio.configure(text="🏠", anchor="center")

    def abrir_menu(self):

        self.menu_expandido = True

        self.grid_columnconfigure(0, minsize= ANCHO_MENU_ABIERTO)

        self.menu_scroll.configure(width=230)

        self.boton_inicio.configure(text="🏠  Inicio", anchor="w")

    def accion_boton(self):
        print("Mostrando inicio")

        if self.menu_expandido:
            self.cerrar_menu()
