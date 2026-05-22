from Solucion.Modo import Modo


class ModoAsustado(Modo):
    def ataca(self, bicho):
        # no ataca por miedo
        pass

    def duerme(self, bicho):
        print(f"{bicho} tiembla de miedo...")

    def __str__(self):
        return "Asustado"
