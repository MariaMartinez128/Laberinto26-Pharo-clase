class Modo:
    def actua(self, bicho):
        self.camina(bicho)
        self.ataca(bicho)
        self.duerme(bicho)

    def camina(self, bicho):
        orien = bicho.obtener_orientacion_aleatoria()
        orien.caminar(bicho)

    def ataca(self, bicho):
        bicho.atacar()

    def duerme(self, bicho):
        raise NotImplementedError

    def es_agresivo(self): return False
    def es_perezoso(self): return False
``