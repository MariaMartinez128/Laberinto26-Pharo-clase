from Solucion.Ente import Ente

class Personaje(Ente):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def buscar_enemigo(self):
        return self.juego.buscar_bicho()

    def ir_a(self, orientacion):
        orientacion.caminar(self)

    def muero(self):
        self.juego.muere_personaje()

    def __str__(self):
        return self.nombre
