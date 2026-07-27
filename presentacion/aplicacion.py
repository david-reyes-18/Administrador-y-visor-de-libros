import customtkinter as ctk
from presentacion.navegacion.navegador_vista import NavegadorVista
from presentacion.navegacion.tipo_vista import TipoVista
from presentacion.vistas.vista_login import VistaLogin
from presentacion.vistas.vista_registro import VistaRegistro
from presentacion.vistas.vista_menu import Menu
from infraestructura.repositorios.repoUsuario import RepositorioUsuario
from Servicios.servicio_login import ServicioInicioSesion
from Servicios.servicio_registro import ServicioRegistro

class App(ctk.CTk):
    
    """
    Clase que maneja toda la aplicacion
    """
    
    def __init__(self):
        super().__init__()
        self.navegador = NavegadorVista(self)
        self.configurar_ventana()
        self.registrar_vista()
        
        self.usuario_actual = None
        self.repositorio_usuarios = RepositorioUsuario()
        self.servicio_login = ServicioInicioSesion(self.repositorio_usuarios)
        self.servicio_registro = ServicioRegistro(self.repositorio_usuarios)
    
    def configurar_ventana(self):
        self.title("Librería Tung Tung")
        self.geometry("1000x720")
        self.minsize(900, 800)
    
    def registrar_vista(self):
        self.navegador.agregar_vista(TipoVista.LOGIN, lambda: VistaLogin(self, self.navegador))
        self.navegador.agregar_vista(TipoVista.REGISTRO, lambda: VistaRegistro(self, self.navegador))
        self.navegador.agregar_vista(TipoVista.MENU, lambda: Menu(self, self.navegador))
    
    def iniciar(self):
        self.navegador.mostrar_vista(TipoVista.LOGIN)
        self.mainloop()
