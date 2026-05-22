from Solucion.Ente import Ente

class Bicho(Ente):
    def __init__(self, modo):
        super().__init__()
        self.modo = modo

    def actua(self):
        self.modo.actua(self)

    def buscar_enemigo(self):
        return self.juego.buscar_personaje(self)

    def muero(self):
        self.juego.muere_bicho(self)

    def obtener_orientacion_aleatoria(self):
        return self.posicion.obtener_orientacion_aleatoria()

    def __str__(self):
        return f"Bicho-{self.modo}"