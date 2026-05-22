class Ente:
    def __init__(self):
        self.vidas = 50
        self.poder = 1
        self.posicion = None
        self.juego = None

    def atacar(self):
        enemigo = self.buscar_enemigo()
        if enemigo:
            enemigo.es_atacado_por(self)

    def es_atacado_por(self, alguien):
        self.vidas -= alguien.poder
        print(f"{self} atacado por {alguien}")
        if self.vidas <= 0:
            self.muero()

    def buscar_enemigo(self): raise NotImplementedError
    def muero(self): raise NotImplementedError

    def esta_vivo(self):
        return self.vidas > 0
