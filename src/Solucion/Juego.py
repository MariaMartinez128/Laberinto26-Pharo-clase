import copy
from Solucion.Personaje import Personaje

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.person = None
        self.prototipo = None

    def agregar_bicho(self, b):
        self.bichos.append(b)

    def agregar_personaje(self, nombre):
        self.person = Personaje(nombre)
        self.person.juego = self
        self.obtener_habitacion(1).entrar(self.person)

    def buscar_bicho(self):
        for b in self.bichos:
            if b.posicion == self.person.posicion and b.esta_vivo():
                return b
        return None

    def buscar_personaje(self, bicho):
        if bicho.posicion == self.person.posicion:
            return self.person

    def obtener_habitacion(self, num):
        return self.laberinto.obtener_habitacion(num)

    def clonar(self):
        return copy.deepcopy(self.prototipo)

    def muere_bicho(self, b):
        print(f"{b} muere")

    def muere_personaje(self):
        print("Fin del juego")
