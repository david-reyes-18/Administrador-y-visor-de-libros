from pathlib import Path

class Rutas:
    
    RAIZ = Path(__file__).parent.parent.parent
    
    ASSETS = RAIZ / "assets"
    
    IMAGENES = ASSETS / "images"
    JSONS = ASSETS / "jsons"
    
    @classmethod
    def get_imagen(cls, imagen: str) -> Path:
        return cls.IMAGENES / imagen
    
    @classmethod
    def get_json(cls, json: str) -> Path:
        return cls.JSONS / json