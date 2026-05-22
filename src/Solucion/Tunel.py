from Solucion.Hoja import Hoja

class Tunel(Hoja):
    def __init__(self):
        super().__init__()
        self.laberinto = None

    def aceptar(self, visitor):
        visitor.visitar_tunel(self)

    def entrar(self, alguien):
        if self.laberinto is None:
            self.laberinto = alguien.juego.clonar()
        self.laberinto.entrar(alguien)

    def es_tunel(self):
        return True