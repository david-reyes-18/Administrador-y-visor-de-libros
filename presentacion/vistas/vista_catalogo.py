import customtkinter as ctk

from Utils.utils import CREMA_TEXTO, GRIS_BORDE, MARRON_MADERA, NEGRO_PANEL, BEIGE_MADERA
from presentacion.vistas.vista_base import VistaBase


class VistaCatalogo(ctk.CTkFrame, VistaBase):

    def __init__(self, padre, navegacion):
        super().__init__(padre, fg_color=NEGRO_PANEL, corner_radius=15, border_width=1, border_color=GRIS_BORDE)
        self.navegacion = navegacion
        self.crear_interfaz()

    def crear_interfaz(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        titulo = ctk.CTkLabel(self, text="📚 Catálogo de libros", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=28, weight="bold"))
        titulo.grid(row=0, column=0, sticky="w", padx=30, pady=(25, 15))

        frame_buscador = ctk.CTkFrame(self, fg_color="transparent")
        frame_buscador.grid(row=1, column=0, sticky="ew", padx=30, pady=(0, 15))
        frame_buscador.grid_columnconfigure(0, weight=1)

        self.entrada_busqueda = ctk.CTkEntry(frame_buscador, height=42, placeholder_text="Buscar libro por título...")
        self.entrada_busqueda.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.boton_buscar = ctk.CTkButton(frame_buscador, text="Buscar", width=100, height=42, fg_color=MARRON_MADERA, hover_color = BEIGE_MADERA, command=self.buscar_libro)
        self.boton_buscar.grid(row=0, column=1)

        self.lista_libros = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.lista_libros.grid(row=2, column=0, sticky="nsew", padx=30, pady=(0, 30))
        self.lista_libros.grid_columnconfigure(0, weight=1)

    def mostrar_libros(self, libros):
        self.limpiar_catalogo()

        for fila, libro in enumerate(libros):
            tarjeta = ctk.CTkFrame(self.lista_libros, height=100, corner_radius=12, fg_color=MARRON_MADERA)
            tarjeta.grid(row=fila, column=0, sticky="ew", padx=5, pady=7)
            tarjeta.grid_columnconfigure(0, weight=1)
            tarjeta.grid_propagate(False)

            label_titulo = ctk.CTkLabel(tarjeta, text=libro.titulo, text_color=CREMA_TEXTO, font=ctk.CTkFont(size=18, weight="bold"))
            label_titulo.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 2))

            label_autor = ctk.CTkLabel(tarjeta, text=libro.autor, text_color=CREMA_TEXTO)
            label_autor.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 15))

            boton_ver = ctk.CTkButton(tarjeta, text="Ver libro", width=100, command=lambda: None)
            boton_ver.grid(row=0, column=1, rowspan=2, padx=20, pady=20)

    def limpiar_catalogo(self):
        for widget in self.lista_libros.winfo_children():
            widget.destroy()

    def buscar_libro(self):
        pass
