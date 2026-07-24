from abc import ABC, abstractmethod

class VistaBase(ABC):
    def __init__(self, master) -> None:
        self.master = master
        
    @abstractmethod
    def crear_interfaz(self) -> None:
        pass
    
    def destruir_interfaz(self) -> None:
        for widget in self.master.winfo_children():
            widget.destroy()
    
    def mostrar_interfaz(self) -> None:
        self.destruir_interfaz()
        self.crear_interfaz()