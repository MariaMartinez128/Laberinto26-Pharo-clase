from Uncategorized.modo import Modo


class Perezoso(Modo):
    def duerme(self, un_bicho):
        """duerme en Perezoso (espera 3 segundos)"""
        print(f"{un_bicho} duerme")
        time.sleep(3) # Delay forSeconds: 3

    def es_perezoso(self):
        return True

    def __str__(self):
        """Equivalente a printOn: aStream"""
        return "Gandulete"