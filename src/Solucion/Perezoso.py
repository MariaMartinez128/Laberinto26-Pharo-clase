import time
from Solucion.Modo import Modo

class Perezoso(Modo):
    def duerme(self, bicho):
        print(f"{bicho} duerme")
        time.sleep(0.5)

    def es_perezoso(self):
        return True

    def __str__(self):
        return "Perezoso"