from Solucion.ElementoMapa import ElementoMapa
from Modificaciones.EfectoPocion import EfectoFuerza, EfectoCuracion


class Pocion(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.efecto = None

    def usar(self, personaje):
        if self.efecto:
            self.efecto.aplicar(personaje)


class PocionFuerza(Pocion):
    def __init__(self):
        super().__init__()
        self.efecto = EfectoFuerza()

    def usar(self, personaje):
        print("✨ Has bebido Poción de Fuerza")
        super().usar(personaje)
        print(f"💪 Tu poder aumentó a {personaje.poder}")

    def __str__(self):
        return "Poción de Fuerza"


class PocionCuracion(Pocion):
    def __init__(self):
        super().__init__()
        self.efecto = EfectoCuracion()

    def usar(self, personaje):
        print("✨ Has bebido Poción de Curación")
        super().usar(personaje)
        print(f"❤️ Tus vidas aumentaron a {personaje.vidas}")

    def __str__(self):
        return "Poción de Curación"