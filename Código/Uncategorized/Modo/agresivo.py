from Uncategorized.modo import Modo


class Agresivo(Modo):
    def duerme(self, un_bicho):
        """duerme en Agresivo (espera 1 segundo)"""
        print(f"{un_bicho} duerme")
        time.sleep(1) # Delay forSeconds: 1

    def es_agresivo(self):
        return True

    def __str__(self):
        """Equivalente a printOn: aStream"""
        return "Agresivo(haagendazs)"