import json
from pathlib import Path


def cargar_json(ruta: Path) -> list:
    if not ruta.exists():
        return []

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_json(ruta: Path, datos: list) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
