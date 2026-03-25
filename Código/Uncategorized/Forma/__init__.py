import random
from abc import ABC

class Forma(ABC):
    def __init__(self):
        self.orientaciones = [] # Equivalente a OrderedCollection new
        self.num = None

    def agregar_orientacion(self, una_or):
        """self orientaciones add: unaOr"""
        self.orientaciones.append(una_or)

    def eliminar_orientacion(self, una_or):
        """self orientaciones remove: unaOr ifAbsent: [^nil]"""
        try:
            self.orientaciones.remove(una_or)
        except ValueError:
            return None

    def obtener_orientacion_aleatoria(self):
        """ind := (1 to: self orientaciones size) atRandom. ^self orientaciones at: ind."""
        if not self.orientaciones:
            return None
        return random.choice(self.orientaciones)

    def poner_en_elemento(self, una_or, un_em):
        """unaOr ponerElemento: unEm enContenedor: self"""
        # Aquí ocurre el doble despacho (Double Dispatch)
        una_or.poner_elementos_en_contenedor(un_em, self)