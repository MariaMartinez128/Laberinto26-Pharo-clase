from Uncategorized.ente import Ente


class Bicho(Ente):
    def __init__(self):
        super().__init__()
        self.modo = None

    def actua(self):
        """actua: delega en el modo"""
        # En Pharo: self modo actua: self
        self.modo.actua(self)

    def buscar_enemigo(self):
        """^self juego buscarPersonaje: self"""
        return self.juego.buscar_personaje(self)

    def es_agresivo(self):
        return self.modo.es_agresivo()

    def es_perezoso(self):
        return self.modo.es_perezoso()

    def muero(self):
        self.juego.muere_bicho(self)

    def __str__(self):
        """Equivalente a printOn: para BichoCR7suuu"""
        return f"BichoCR7suuu {self.modo}"