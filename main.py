import sys
sys.dont_write_bytecode = True

from presentacion.aplicacion import App

if __name__ == "__main__":
    app = App()
    app.iniciar()
