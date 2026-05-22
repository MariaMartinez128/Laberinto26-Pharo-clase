class EfectoPocion:
    def aplicar(self, personaje):
        raise NotImplementedError


class EfectoFuerza(EfectoPocion):
    def aplicar(self, personaje):
        personaje.poder += 5


class EfectoCuracion(EfectoPocion):
    def aplicar(self, personaje):
        personaje.vidas += 10