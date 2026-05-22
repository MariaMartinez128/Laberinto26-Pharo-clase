import sys
import os

# Agregar el directorio src al path para los imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Builder.Director import Director
from Modificaciones.ConsolaInteractiva import ConsolaInteractiva


if __name__ == "__main__":
    # Procesar el JSON del laberinto
    director = Director()
    director.procesar("laberinto.json")

    # Obtener el juego
    juego = director.obtener_juego()

    # Iniciar la consola interactiva
    consola = ConsolaInteractiva(juego)
    consola.loop()

