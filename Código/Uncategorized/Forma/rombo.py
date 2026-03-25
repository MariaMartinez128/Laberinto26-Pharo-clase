from Uncategorized.forma import Forma


class Rombo(Forma):
    def __init__(self):
        super().__init__()
        self.ne = None # Noreste
        self.no = None # Noroeste
        self.se = None # Sureste
        self.so = None # Suroeste

    # Métodos setter para las clases Orientacion correspondientes
    def set_noreste(self, un_em):  self.ne = un_em
    def set_noroeste(self, un_em): self.no = un_em
    def set_sureste(self, un_em):  self.se = un_em
    def set_suroeste(self, un_em): self.so = un_em