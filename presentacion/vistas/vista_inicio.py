import customtkinter as ctk

from Utils.utils import BEIGE_MADERA, CREMA_TEXTO, GRIS_BORDE, MARRON_MADERA, MARRON_OSCURO, NEGRO_PANEL
from presentacion.vistas.vista_base import VistaBase
from presentacion.navegacion.tipo_vista import TipoVista

class VistaInicio(ctk.CTkFrame, VistaBase):

    def __init__(self, padre, navegacion):
        super().__init__(padre, fg_color=NEGRO_PANEL, corner_radius=15, border_width=1, border_color=GRIS_BORDE)
        self.navegacion = navegacion
        self.crear_interfaz()

    def crear_interfaz(self):
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(3, weight=1)

        titulo = ctk.CTkLabel(self, text="¡Bienvenido Pibardo!", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=30, weight="bold"))
        titulo.grid(row=0, column=0, columnspan=3, sticky="w", padx=30, pady=(30, 5))

        descripcion = ctk.CTkLabel(self, text="Explora el catálogo, encuentra nuevos libros y continúa tus lecturas.", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=16))
        descripcion.grid(row=1, column=0, columnspan=3, sticky="w", padx=30, pady=(0, 25))

        tarjeta_catalogo = ctk.CTkFrame(self, height=150, corner_radius=15, fg_color=MARRON_OSCURO, border_width=1, border_color=GRIS_BORDE)
        tarjeta_catalogo.grid(row=2, column=0, sticky="nsew", padx=(30, 8), pady=(0, 20))
        tarjeta_catalogo.grid_propagate(False)

        icono_catalogo = ctk.CTkLabel(tarjeta_catalogo, text="📚", font=ctk.CTkFont(size=34))
        icono_catalogo.pack(pady=(18, 5))

        texto_catalogo = ctk.CTkLabel(tarjeta_catalogo, text="Explorar catálogo", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=17, weight="bold"))
        texto_catalogo.pack()

        boton_catalogo = ctk.CTkButton(tarjeta_catalogo, text="Ver libros", width=120, height=32, fg_color=MARRON_MADERA, hover_color=BEIGE_MADERA, text_color=CREMA_TEXTO, command=lambda: self.navegacion.mostrar_contenido(TipoVista.CATALOGO, self.master))
        boton_catalogo.pack(pady=12)

        tarjeta_lecturas = ctk.CTkFrame(self, height=150, corner_radius=15, fg_color=MARRON_OSCURO, border_width=1, border_color=GRIS_BORDE)
        tarjeta_lecturas.grid(row=2, column=1, sticky="nsew", padx=8, pady=(0, 20))
        tarjeta_lecturas.grid_propagate(False)

        icono_lecturas = ctk.CTkLabel(tarjeta_lecturas, text="📖", font=ctk.CTkFont(size=34))
        icono_lecturas.pack(pady=(18, 5))

        texto_lecturas = ctk.CTkLabel(tarjeta_lecturas, text="Mis lecturas", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=17, weight="bold"))
        texto_lecturas.pack()

        boton_lecturas = ctk.CTkButton(tarjeta_lecturas, text="Continuar", width=120, height=32, fg_color=MARRON_MADERA, hover_color=BEIGE_MADERA, text_color=CREMA_TEXTO, command=lambda: None)
        boton_lecturas.pack(pady=12)

        tarjeta_perfil = ctk.CTkFrame(self, height=150, corner_radius=15, fg_color=MARRON_OSCURO, border_width=1, border_color=GRIS_BORDE)
        tarjeta_perfil.grid(row=2, column=2, sticky="nsew", padx=(8, 30), pady=(0, 20))
        tarjeta_perfil.grid_propagate(False)

        icono_perfil = ctk.CTkLabel(tarjeta_perfil, text="👤", font=ctk.CTkFont(size=34))
        icono_perfil.pack(pady=(18, 5))

        texto_perfil = ctk.CTkLabel(tarjeta_perfil, text="Mi perfil", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=17, weight="bold"))
        texto_perfil.pack()

        boton_perfil = ctk.CTkButton(tarjeta_perfil, text="Ver perfil", width=120, height=32, fg_color=MARRON_MADERA, hover_color=BEIGE_MADERA, text_color=CREMA_TEXTO, command=lambda: self.navegacion.mostrar_contenido(TipoVista.PERFIL, self.master))
        boton_perfil.pack(pady=12)

        panel_inferior = ctk.CTkFrame(self, corner_radius=15, fg_color=MARRON_OSCURO, border_width=1, border_color=GRIS_BORDE)
        panel_inferior.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=30, pady=(0, 30))
        panel_inferior.grid_columnconfigure(0, weight=1)
        panel_inferior.grid_rowconfigure(1, weight=1)

        titulo_panel = ctk.CTkLabel(panel_inferior, text="Recomendaciones para ti", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=21, weight="bold"))
        titulo_panel.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 10))

        contenido_vacio = ctk.CTkLabel(panel_inferior, text="Aquí aparecerán libros recomendados.", text_color=CREMA_TEXTO, font=ctk.CTkFont(size=15))
        contenido_vacio.grid(row=1, column=0, padx=20, pady=20)
