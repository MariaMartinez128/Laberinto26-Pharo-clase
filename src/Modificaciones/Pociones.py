class Pocion:
    def usar(self, personaje):
        pass


class PocionFuerza(Pocion):
    def usar(self, personaje):
        personaje.poder += 5
        print("Poder aumentado +5")


class PocionCuracion(Pocion):
    def usar(self, personaje):
        personaje.vidas += 10
        print("Curación +10")
``