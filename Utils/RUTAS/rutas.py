from pathlib import Path


RUTA_BASE_IMAGENES = Path(__file__).resolve().parent.parent.parent
RUTA_BASE_DATOS = Path(__file__).resolve().parent.parent

RUTA_DATOS = RUTA_BASE_DATOS / "JSON"/ "DATOS"
RUTA_USUARIOS = RUTA_DATOS / "usuarios.json"

RUTA_IMAGENES = RUTA_BASE_IMAGENES / "Imagenes"
FONDO = RUTA_IMAGENES / "Fondo.png"
BRR_PATAPIM = RUTA_IMAGENES / "Brr_patapim.png"
