import customtkinter as ctk
from PIL import Image
from infraestructura.manejador_rutas.rutas import Rutas


NEGRO_FONDO = "#0B0B0B"
NEGRO_PANEL = "#151515"
MARRON_OSCURO = "#2A1C16"
MARRON_MADERA = "#5A3825"
BEIGE_MADERA = "#C6A27E"
CREMA_TEXTO = "#E8D7C3"
ROJO_ACENTO = "#8F2D2D"
ROJO_HOVER = "#A63A3A"
GRIS_BORDE = "#3A332F"

ANCHO = 1920
ALTO = 1080


IMG_FONDO = ctk.CTkImage(dark_image=Image.open(Rutas.get_imagen("Fondo.png")), size=(ANCHO, ALTO))
BRR_PATAPIMES = ctk.CTkImage(dark_image=Image.open(Rutas.get_imagen("Brr_patapim.png")), size=(450, 480))
