from Solucion.Modo import Modo


class ModoFrenetico(Modo):
    def ataca(self, bicho):
        print(f"{bicho} ¡ataca furiosamente!")

    def duerme(self, bicho):
        print(f"{bicho} no duerme, ¡sigue atacando!")

    def __str__(self):
        return "Frenetico"
