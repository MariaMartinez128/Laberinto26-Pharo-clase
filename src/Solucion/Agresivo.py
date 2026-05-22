import time

class Agresivo(Modo):
    def duerme(self, bicho):
        print(f"{bicho} duerme")
        time.sleep(1)

    def es_agresivo(self):
        return True

    def __str__(self):
        return "Agresivo"
``
``