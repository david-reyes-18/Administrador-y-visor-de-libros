import json
from pathlib import Path

class ManejadorJSON:
    
    """
    Manejador para operaciones con archivos JSON.
    """
    
    @staticmethod
    def cargar_json(ruta: Path) -> list | dict:
        if not ruta.exists():
            return []
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    
    @staticmethod
    def guardar_json(ruta: Path, datos: list | dict) -> None:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
