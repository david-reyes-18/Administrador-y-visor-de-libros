from collections.abc import Callable

import customtkinter as ctk

from presentacion.navegacion.tipo_vista import TipoVista

class NavegadorVista:
    def __init__(self, master):
        self.master = master
        self.vistas: dict[TipoVista, Callable[[], ctk.CTkFrame]] = {}
        self.vista_actual: ctk.CTkFrame | None = None
        self.tipo_vista_actual: TipoVista | None = None

    def agregar_vista(
        self,
        tipo_vista: TipoVista,
        crear_vista: Callable[[], ctk.CTkFrame],
    ):
        self.vistas[tipo_vista] = crear_vista
    
    def mostrar_vista(self, tipo_vista: TipoVista):
        crear_vista = self.vistas.get(tipo_vista)
        if crear_vista is None:
            raise ValueError(f"La vista {tipo_vista.name} no está registrada.")

        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = crear_vista()
        self.vista_actual.place(x=0, y=0, relwidth=1, relheight=1)
        self.tipo_vista_actual = tipo_vista
