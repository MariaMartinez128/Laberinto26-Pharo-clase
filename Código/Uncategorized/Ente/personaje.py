from Uncategorized.ente import Ente


class Personaje(Ente):
    def __init__(self, nombre="Sin nombre"):
        super().__init__()
        self.nombre = nombre

    def buscar_enemigo(self):
        """Pide al juego un bicho en su posición"""
        return self.juego.obtener_bicho_en(self.posicion)

    def ir_a(self, una_or):
        """unaOr caminar: self"""
        una_or.caminar(self)

    def muero(self):
        self.juego.muere_personaje()

    def __str__(self):
        """Equivalente a printOn: para El bueno de..."""
        return f"El bueno de {self.nombre}"