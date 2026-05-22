import random

class Forma:
    def __init__(self):
        self.orientaciones = []
        self.num = None

    def agregar_orientacion(self, o):
        self.orientaciones.append(o)

    def eliminar_orientacion(self, o):
        if o in self.orientaciones:
            self.orientaciones.remove(o)

    def obtener_elemento(self, orientacion):
        return orientacion.obtener_elemento(self)

    def obtener_orientacion_aleatoria(self):
        return random.choice(self.orientaciones)

    def poner_en(self, orientacion, em):
        orientacion.poner_elemento(em, self)