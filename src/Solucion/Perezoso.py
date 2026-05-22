class Perezoso(Modo):
    def duerme(self, bicho):
        print(f"{bicho} duerme")
        time.sleep(3)

    def es_perezoso(self):
        return True

    def __str__(self):
        return "Perezoso"
        return "Perezoso"