
from abc import ABC, abstractmethod

class RutaNavegacion(ABC):
    rutas_registradas: list[type["RutaNavegacion"]] = []
    destino: str = ""

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.destino:
            RutaNavegacion.rutas_registradas.append(cls)

    def __init__(self, navegacion):
        self.navegacion = navegacion

    def mostrar(self, clase_vista, titulo):
        ventana = self.navegacion.ventana
        ventana.title(titulo)

        nombre_vista = self.destino

        if nombre_vista not in self.navegacion.vistas:

            vista = clase_vista(padre=ventana, navegacion=self.navegacion)
            vista.place(x=0, y=0, relwidth=1, relheight=1)
            self.navegacion.vistas[nombre_vista] = vista

        nueva_vista = self.navegacion.vistas[nombre_vista]
        nueva_vista.tkraise()
        self.navegacion.frame_actual = nueva_vista

    @abstractmethod
    def ejecutar(self) -> None:
        """Ejecuta la navegación correspondiente."""
        pass
