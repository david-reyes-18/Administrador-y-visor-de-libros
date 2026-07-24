import customtkinter as ctk

from .nave_asbstracta import RutaNavegacion, NavegadorAbstracto
from Vistas.vistaLogin import VistaLogin
from Vistas.vistaRegistro import VistaRegistro 
from Utils.JSON.Repositorios.repoUsuario import RepositorioUsuario
from Servicios.servicio_login import ServicioInicioSesion
from Servicios.servicio_registro import ServicioRegistro

class Navegacion:

    def __init__(self):
        self.ventana = ctk.CTk()
        self.vistas = {}
        self.ventana.title("Librería Tung Tung")
        self.ventana.geometry("1000x720")
        self.ventana.minsize(760, 620)
        self.ventana.attributes("-fullscreen", True)
        self.usuario_actual = None
        self.frame_actual = None
        self.repositorio_usuarios = RepositorioUsuario()
        self.servicio_inicio_sesion = ServicioInicioSesion(self.repositorio_usuarios)
        self.servicio_registro = ServicioRegistro(self.repositorio_usuarios)
        self.navegador = NavegadorRutas(self)

    def iniciar(self):
        self.navegar("login")
        self.ventana.mainloop()

    def navegar(self, destino):
        self.navegador.navegar(destino)



class NavegadorRutas(NavegadorAbstracto):

    def __init__(self, navegacion):
        self.rutas = {
            clase_ruta.destino: clase_ruta(navegacion)
            for clase_ruta in RutaNavegacion.rutas_registradas
        }

    def navegar(self, destino):
        ruta = self.rutas.get(destino)

        if ruta is None:
            raise ValueError(f"La ruta '{destino}' no está registrada.")

        ruta.ejecutar()


class RutaLogin(RutaNavegacion):
    destino = "login"

    def ejecutar(self):
        self.mostrar(clase_vista=VistaLogin, titulo="Inicio de sesión - Librería Tung Tung")

class RutaRegistro(RutaNavegacion):
    destino = "registro"

    def ejecutar(self):
        self.mostrar(clase_vista=VistaRegistro, titulo="Registro - Librería Tung Tung")